from PIL import Image as PilImage
from app.settings import VALID_FORMATS
from rest_framework import serializers
from typing import Tuple


class ImageFormatValidator:
    def __init__(self, valid_formats: Tuple[str] = VALID_FORMATS):
        self.valid_formats = valid_formats

    def __call__(self, value: str):
        image = PilImage.open(value)
        _format = image.format.upper()

        if _format not in self.valid_formats:
            raise serializers.ValidationError(f'Only {",".join(self.valid_formats)} formats are supported.')
