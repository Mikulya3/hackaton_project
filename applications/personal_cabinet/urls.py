from django.urls import path, include
from rest_framework.routers import DefaultRouter

from applications.personal_cabinet.views import UserProfileAPIView, MentorProfileAPIView, PaymentMethodAPIView

router = DefaultRouter()
router.register('UserProfile', UserProfileAPIView),
router.register('MentorProfile', MentorProfileAPIView),


urlpatterns = [
    path('payment/', PaymentMethodAPIView.as_view()),
    path('', include(router.urls)),
]
