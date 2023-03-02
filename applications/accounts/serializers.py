from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from applications.accounts.models import Teaching, ClassRoom, CustomUser
from applications.accounts.tasks import send_confirmation_code, send_confirmation_email

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, allow_blank=False, max_length=100)
    email = serializers.EmailField(required=True)
    experience = serializers.CharField(required=True, max_length=20)
    is_mentor = serializers.BooleanField(required=True)
    password = serializers.CharField(required=True, min_length=6)
    password2 = serializers.CharField(required=True, min_length=6)
    class Meta:
        model = User
        fields = ['email', 'username', 'experience', 'is_mentor', 'password', 'password2']

    def validate(self, attrs):
        p1 = attrs.get('password')
        p2 = attrs.pop('password2')

        if p1 != p2:
            raise serializers.ValidationError('Пароли не совпадают!')

        return attrs


    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.create_activation_code()
        send_confirmation_email(user.email, user.activation_code)
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    def validate_email(self, email):
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Пользователь не зарегистрирован')
        return email

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(username=email,
                                password=password)


        if not user:
            raise serializers.ValidationError('Неверный email или пароль')
        attrs['user'] = user
        return attrs


        return user

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(
        required=True,
        min_length=6
    )
    new_password_confirm = serializers.CharField(
        required=True,
        min_length=6
    )

    def validate(self, attrs):
        p1 = attrs.get('new_password')
        p2 = attrs.get('new_password_confirm')
        if p1 != p2:
            raise serializers.ValidationError('Пароли не совпадают!')
        return attrs

    def validate_old_password(self, p):
        request = self.context.get('request')
        user = request.user
        if not user.check_password(p):
            raise serializers.ValidationError('Неверный пароль!')
        return p

    def set_new_password(self):
        user = self.context.get('request').user
        password = self.validated_data.get('new_password')
        user.set_password(password)
        user.save()


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def validate_email(self, email):
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Пользователь с такой почтой не существует!')
        return email

    def send_code(self):
        email = self.validated_data.get('email')
        user = User.objects.get(email=email)
        user.create_activation_code()
        user.save()
        send_confirmation_code(email, user.activation_code)


class ForgotPasswordCompleteSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    code = serializers.CharField(required=True)
    password = serializers.CharField(required=True, min_length=6)
    password_confirm = serializers.CharField(required=True, min_length=6)

    def validate_email(self, email):
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError('пользователь не зарегистрирован!')
        return email

    @staticmethod
    def validate_code(code):
        if not User.objects.filter(activation_code=code).exists():
            raise serializers.ValidationError('Неверный код!')
        return code


def validate(self, attrs):
        p1 = attrs.get('password')
        p2 = attrs.get('password_confirm')

        if p1 != p2:
            raise serializers.ValidationError('пароли не совпадают!')
        return attrs


def set_new_password(self):
    email = self.validated_data.get('email')
    password = self.validated_data.get('password')
    user = User.objects.get(email=email)
    user.set_password(password)
    user.activation_code = ''
    user.save()


class TeachingSerializer(serializers.Serializer):
    question = serializers.CharField(max_length=500)
    answer = serializers.ChoiceField(choices=Teaching.ANSWERS)


class ClassRoomSerializer(serializers.Serializer):
    question = serializers.CharField(max_length=500)
    answer = serializers.ChoiceField(choices=ClassRoom.ANSWERS)
