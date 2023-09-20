import factory
from django.contrib.auth.models import User
from images.models import UserProfile, Tier


class TierFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tier

    name = 'Basic'
    thumbnail_sizes = "['200x200']"
    generate_expiring_links = False
    include_original_link = False


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    password = factory.PostGenerationMethodCall('set_password', 'password')

    @factory.post_generation
    def create_user_profile(self, created, extracted, **kwargs):
        if created:
            UserProfile.objects.create(user=self, tier=TierFactory())


class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserProfile
