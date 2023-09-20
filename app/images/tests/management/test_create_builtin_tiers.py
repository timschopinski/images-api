from django.test import TestCase
from django.core.management import call_command
from images.models import Tier
from app.settings import BUILTIN_TIERS
from images.utils import convert_thumbnail_sizes_to_list


class CreateBuiltInTiersCommandTestCase(TestCase):
    def test_create_builtin_tiers(self):
        self.assertEqual(Tier.objects.count(), 0)

        call_command('create_builtin_tiers')

        for tier_name, tier_data in BUILTIN_TIERS.items():
            tier = Tier.objects.get(name=tier_name)
            self.assertEqual(
                convert_thumbnail_sizes_to_list(tier.thumbnail_sizes),
                tier_data['thumbnail_sizes']
            )
            self.assertEqual(tier.include_original_link, tier_data['include_original_link'])
            self.assertEqual(tier.generate_expiring_links, tier_data['generate_expiring_links'])

        self.assertEqual(Tier.objects.count(), len(BUILTIN_TIERS))
