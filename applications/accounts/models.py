from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _



class UserQuerySet(models.QuerySet):
    pass

class UserManager(BaseUserManager):
    use_in_migrations = True

    def get_queryset(self):
        return UserQuerySet(self.model, using=self._db)

    def _create_user(self, username=None, email=None, password=None, **extra_fields):
        if not email:
            raise ValueError(_("Users must have an email address"))

        fullname = username.split()
        if len(fullname) <= 1:
            raise ValidationError(
                _('Kindly enter more than one name.'),
                code='invalid',
                params={'value': self},
            )
        for i in fullname:
            if len(i) < 2:
                raise ValidationError(
                    _('Kindly give us your full name.'),
                    code='invalid',
                    params={'value': self},
                )
        email = self.normalize_email(email)
        username = ' '.join(map(str, fullname))
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)


    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Admin must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Admin must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)




    def __str__(self):
        return f'{self.name} {self.surname}'

class Teaching(models.Model):
    ANSWERS= (
        ('лично, частным образом', 'лично, частным образом'),
        ('лично, профессионально', 'лично, профессионально'),
        ('онлайн', 'онлайн'),
        ('другое', 'другое'),
    )
    question = models.CharField(max_length=500,default=True)
    answer = models.CharField(max_length=50, choices=ANSWERS, null=False, blank=False)



    def __str__(self):
        return self.answer


class ClassRoom(models.Model):
    ANSWERS = (
        ('в настоящий момент нет', 'в настоящий момент нет'),
        ('у меня маленькая аудитория', 'у меня маленькая аудитория'),
        ('у меня достаточная аудитория', 'у меня достаточная аудитория'),

    )
    question = models.CharField(max_length=500, default=True)
    answer = models.CharField(max_length=50, choices=ANSWERS, null=True, blank=True,default=True)

    def __str__(self):
        return self.answer



class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'), unique=True, max_length=255)
    email = models.EmailField(_('email'), unique=True, null=True, blank=True)
    is_active = models.BooleanField(_('active'), default=False)
    is_staff = models.BooleanField(_('staff'), default=False)
    is_verified = models.BooleanField(_('verified'), default=False)
    type = models.CharField('type', max_length=100,default=True)
    password = models.SlugField('password', max_length=100)
    experience = models.CharField('experience', max_length=50,default=0)
    is_mentor = models.BooleanField('is_mentor', default=False)


    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')


