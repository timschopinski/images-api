from django.core.management.base import BaseCommand
from images.models import Tier
from app.settings import BUILTIN_TIERS


class Command(BaseCommand):
    help = 'Ensure the creation of three built-in tiers'

    def handle(self, *args, **options):
        for tier_name, tier_data in BUILTIN_TIERS.items():
            tier, created = Tier.objects.get_or_create(name=tier_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created tier: {tier.name}'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Tier already exists: {tier.name}'))

            tier.thumbnail_sizes = tier_data['thumbnail_sizes']
            tier.include_original_link = tier_data['include_original_link']
            tier.generate_expiring_links = tier_data['generate_expiring_links']

            tier.save()

        self.stdout.write(self.style.SUCCESS('Built-in tiers creation completed'))
