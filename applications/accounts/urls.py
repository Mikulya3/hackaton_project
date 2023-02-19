from django.urls.conf import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (RegisterApiView, ChangePasswordApiView, ActivationApiView, ForgotPasswordAPIView,
                    ForgotPasswordCompleteAPIView, TeachingViewSet, ClassRoomViewSet)



urlpatterns = [
    path('register/',RegisterApiView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('change_password/', ChangePasswordApiView.as_view()),
    path('activate/<uuid:activation_code>/', ActivationApiView.as_view()),
    path('forgot_password/', ForgotPasswordAPIView.as_view()),
    path('forgot_password_complete/', ForgotPasswordCompleteAPIView.as_view()),
    path('q1/', TeachingViewSet.as_view({'get': 'list'})),
    path('q2/', ClassRoomViewSet.as_view({'get': 'list'})),

]