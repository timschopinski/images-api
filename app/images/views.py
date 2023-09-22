from rest_framework import viewsets
from .models import Image
from .serializers import ImageSerializer, ExpiringLinkSerializer
from rest_framework import permissions
from .utils import create_thumbnails
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
import boto3
from app.settings import AWS_ACCESS_KEY_ID, \
                         AWS_STORAGE_BUCKET_NAME, AWS_SECRET_ACCESS_KEY


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Image.objects.filter(user=self.request.user.id)

    def perform_create(self, serializer: ImageSerializer):
        user = self.request.user
        image = serializer.save(user=user)
        create_thumbnails(image)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        user_tier = request.user.userprofile.tier
        if user_tier and not user_tier.include_original_link:
            for item in serializer.data:
                item.pop('image', None)

        return Response(serializer.data, status=status.HTTP_200_OK)


class GenerateExpiringLinkView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def post(request):
        serializer = ExpiringLinkSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            if request.user.userprofile.tier.name != 'Enterprise':
                return Response(
                    {'error': 'Access denied. User is not on the Enterprise plan.'},
                    status=status.HTTP_403_FORBIDDEN
                )
            image = serializer.validated_data['image']
            expiration_seconds = serializer.validated_data['expiration_seconds']
            Image.objects.filter(user=request.user, image=image).first()
            if not Image.objects.filter(user=request.user, image=image).first():
                return Response(
                    {'error': 'Requested image does not belong to the user.'},
                    status=status.HTTP_403_FORBIDDEN
                )

            s3 = boto3.client(
                's3',
                aws_access_key_id=AWS_ACCESS_KEY_ID,
                aws_secret_access_key=AWS_SECRET_ACCESS_KEY
            )
            url = s3.generate_presigned_url(
                'get_object',
                Params={'Bucket': AWS_STORAGE_BUCKET_NAME, 'Key': image},
                ExpiresIn=expiration_seconds
            )
            return Response({'url': url})

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
