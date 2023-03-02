from django.urls import path
from .views import FavoriteAPIView
from django.urls import path, include

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', FavoriteAPIView)

urlpatterns = [
    path('', include(router.urls)),
]
