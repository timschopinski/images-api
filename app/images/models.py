from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


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

    def __str__(self):
        return self.image.name


class Thumbnail(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='thumbnails')
    size = models.CharField(max_length=20)
    thumbnail = models.ImageField(upload_to='thumbnails/')

    def __str__(self):
        return f'{self.thumbnail.name}-thumbnail-{self.size}'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tier = models.ForeignKey(Tier, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "User Profiles"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance: User, created: bool, **kwargs):
    if created:
        basic_tier, _ = Tier.objects.get_or_create(name='Basic')
        try:
            instance.userprofile.tier
        except models.ObjectDoesNotExist:
            UserProfile.objects.get_or_create(user=instance, tier=basic_tier)
