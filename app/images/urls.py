from rest_framework.routers import DefaultRouter
from .views import ImageViewSet, GenerateExpiringLinkView
from django.urls import path, include


router = DefaultRouter()
router.register('images', ImageViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/generate-expiring-link/', GenerateExpiringLinkView.as_view(), name='generate_expiring_link'),
]
