import os
from io import BytesIO
from typing import List

from PIL import Image as PilImage
from django.core.files.base import ContentFile
from .models import Image, Thumbnail


def resize_image(image, width, height):
    try:
        img = PilImage.open(image)
        img = img.resize((width, height))

        _format = PilImage.open(image).format.upper()
        img_buffer = BytesIO()
        img.save(img_buffer, format=_format)
        img_buffer.seek(0)

        return img_buffer

    except Exception as e:
        raise e


def convert_thumbnail_sizes_to_list(thumbnail_sizes: str) -> List[str]:
    return [size.strip() for size in thumbnail_sizes[1:-1].replace("'", "").split(',')]


def create_thumbnails(image: Image):
    thumbnail_sizes = convert_thumbnail_sizes_to_list(
        image.user.userprofile.tier.thumbnail_sizes
    )

    for size in thumbnail_sizes:
        width, height = map(int, size.split('x'))
        resized_image_buffer = resize_image(image.image, width, height)

        original_extension = os.path.splitext(image.image.name)[-1]
        thumbnail_extension = f'-thumbnail-{size}{original_extension}'

        thumbnail_content = ContentFile(resized_image_buffer.getvalue())
        thumbnail_name = os.path.splitext(os.path.basename(image.image.name))[0] + thumbnail_extension

        thumbnail = Thumbnail.objects.create(image=image, size=size)
        thumbnail.thumbnail.save(thumbnail_name, thumbnail_content, save=True)
