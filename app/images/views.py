from rest_framework import viewsets
from .models import Image
from .serializers import ImageSerializer
from rest_framework import permissions


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Image.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
