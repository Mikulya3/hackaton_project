from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import UserProfile, PaymentMethod, MentorProfile
from .serializers import UserProfileSerializer, MentorProfileSerializer


class UserProfileAPIView(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class MentorProfileAPIView(ModelViewSet):
    queryset = MentorProfile.objects.all()
    serializer_class = MentorProfileSerializer


class PaymentMethodAPIView(APIView):

    def get(self, request):
        user_profile = UserProfile.objects.get(user=request.user)
        payment_methods = PaymentMethod.objects.filter(user_profile=user_profile)
        context = {'payment_methods': payment_methods}
        return render(request, context)
