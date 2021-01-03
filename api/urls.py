
from django.urls import path,include
from rest_framework import routers
from .views import ShortenerViewSet
router = routers.DefaultRouter()
router.register('', ShortenerViewSet)

urlpatterns = router.urls

