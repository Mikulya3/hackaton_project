from rest_framework import serializers

from applications.accounts.serializers import ChangePasswordSerializer
from applications.personal_cabinet.models import UserProfile, MentorProfile, PaymentMethod


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

    def validate(self, attrs):
        new_password = attrs.get('new_password')
        if new_password:
            data = {
                'old_password': attrs.get('password'),
                'new_password': new_password,
                'new_password_confirm': attrs.get('new_password_confirm'),
            }
            serializer = ChangePasswordSerializer(data=data, context=self.context)
            serializer.is_valid(raise_exception=True)
        return attrs

class MentorProfileSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(max_length=None, use_url=True, required=False)
    class Meta:
        model = MentorProfile
        fields = '__all__'


class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = '__all__'
