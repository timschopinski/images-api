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

    username = factory.Sequence(lambda n: f'user{n}')
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    password = factory.PostGenerationMethodCall('set_password', 'password123#')

    @factory.post_generation
    def create_user_profile(self, created, extracted, **kwargs):
        if created:
            user_profile = UserProfile.objects.get(user=self)
            user_profile.tier = TierFactory()
            user_profile.save()


class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserProfile
