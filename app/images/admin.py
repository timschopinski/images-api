from .models import Tier, Image
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserProfile


class TierAdmin(admin.ModelAdmin):
    list_display = ('name', 'generate_expiring_links', 'include_original_link', 'thumbnail_sizes')
    list_filter = ('generate_expiring_links', 'include_original_link')
    search_fields = ('name',)


class ImageAdmin(admin.ModelAdmin):
    list_display = ('user', 'image', 'uploaded_at')
    list_filter = ('user',)
    search_fields = ('user__username',)


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'User Profiles'


class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'get_user_tier')

    def get_user_tier(self, obj):
        try:
            return obj.userprofile.tier.name
        except UserProfile.DoesNotExist:
            return "N/A"

    get_user_tier.short_description = 'User Tier'


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

admin.site.register(Tier, TierAdmin)
admin.site.register(Image, ImageAdmin)
