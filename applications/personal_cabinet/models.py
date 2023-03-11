from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from main import settings

User = get_user_model()

class UserProfile(models.Model):
    LANG_CHOICES = (
        ('ru', 'Russian'),
        ('en', 'English'),
        ('kg', 'Kyrgyz'),
        ('tr', 'Turkish'),
        ('es', 'Español'),
        ('fr', 'Français'),
        ('de', 'Deutsch'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={'is_mentor': False})
    name = models.CharField(max_length=50, editable=True)
    surname = models.CharField(max_length=75, editable=True)
    core_competence = models.CharField(max_length=60, editable=True)
    language = models.CharField(max_length=2, choices=LANG_CHOICES, editable=True)
    website = models.URLField(blank=True, editable=True)
    twitter = models.URLField(blank=True, editable=True)
    facebook = models.URLField(blank=True, editable=True)
    linkedin = models.URLField(blank=True, editable=True)
    youtube = models.URLField(blank=True, editable=True)
    photo = models.ImageField(upload_to='profile_photos/', blank=True, editable=True)
    promotions = models.BooleanField(default=True)
    course_recommendations = models.BooleanField(default=True)
    helpful_resources = models.BooleanField(default=True)
    teacher_announcements = models.BooleanField(default=True)
    receive_promotional_emails = models.BooleanField(default=True)
    unsubscribe = models.BooleanField(default=False, editable=True)
    show_profile = models.BooleanField(default=True, editable=True)
    show_courses = models.BooleanField(default=True, editable=True)

    def __str__(self):
        return self.user.username

    def get_photo(self):
        if self.photo:
            return self.photo.url
        else:
            return None

    def close_account(self):
        if self.user.course_set.exists():
            return 'if you close your account, your registration for all courses will be canceled and you will lose access to them forever'
        else:
            self.user.paymentmethod_set.all().delete()
            self.user.delete()
            return 'your account was successfully closed'

class PaymentMethod(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    stripe_payment_method_id = models.CharField(max_length=50)
    card_brand = models.CharField(max_length=50)
    card_last4 = models.CharField(max_length=4)
    exp_month = models.IntegerField()
    exp_year = models.IntegerField()

    def __str__(self):
        return f'{self.card_brand} **** **** {self.card_last4}'





class MentorProfile(models.Model):
    LANG_CHOICES = (
        ('ru', 'Russian'),
        ('en', 'English'),
        ('kg', 'Kyrgyz'),
        ('tr', 'Turkish'),
        ('es', 'Español'),
        ('fr', 'Français'),
        ('de', 'Deutsch'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='mentor_profile', limit_choices_to={'is_mentor':True})
    name = models.CharField(max_length=50, editable=True)
    surname = models.CharField(max_length=75, editable=True)
    core_competence = models.CharField(max_length=60, editable=True)
    biography = models.CharField(max_length=50, editable=True)
    language = models.CharField(max_length=2, choices=LANG_CHOICES, editable=True)
    photo = models.ImageField(upload_to='mentor_profile_photo/', blank=True, null=True, editable=True, height_field='image_height', width_field='image_width')
    show_profile = models.BooleanField(default=True, editable=True)
    show_courses = models.BooleanField(default=True, editable=True)
    website = models.URLField(blank=True, editable=True)
    twitter = models.URLField(blank=True, editable=True)
    facebook = models.URLField(blank=True, editable=True)
    linkedin = models.URLField(blank=True, editable=True)
    youtube = models.URLField(blank=True, editable=True)

    def __str__(self):
        return self.user.username

    def get_photo(self):
        if self.photo:
            return self.photo.url
        else:
            return None

@receiver(signal=post_save, sender=MentorProfile)
def send_notification(sender, instance, created, **kwargs):
    if not created:
        user = instance.user
        notification = f'your profile privacy settings have been updated'
        user.notification.create(notification=notification)

