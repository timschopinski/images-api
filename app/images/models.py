from django.contrib.auth.models import User
from django.db import models


class Tier(models.Model):
    name = models.CharField(max_length=50)
    thumbnail_sizes = models.CharField(
        max_length=255,
        help_text="Comma-separated list of thumbnail sizes (e.g., '200x200,400x400').",
    )
    generate_expiring_links = models.BooleanField(
        default=False,
        help_text="Enable generating expiring links for images."
    )
    include_original_link = models.BooleanField(
        default=False,
        help_text="Include a link to the originally uploaded image."
    )

    def __str__(self):
        return self.name


class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tier = models.ForeignKey(Tier, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "User Profiles"
