from rest_framework import serializers
from .models import Image, Thumbnail
from .validators import ImageFormatValidator


class ThumbnailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thumbnail
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(validators=[ImageFormatValidator()])
    thumbnails = ThumbnailSerializer(many=True, read_only=True)

    class Meta:
        model = Image
        fields = '__all__'
        read_only_fields = ('user',)


class ExpiringLinkSerializer(serializers.Serializer):
    expiration_seconds = serializers.IntegerField(
        min_value=300, max_value=30000,
        help_text="Expiration time in seconds (between 300 and 30000)"
    )
    image = serializers.CharField(write_only=True)
