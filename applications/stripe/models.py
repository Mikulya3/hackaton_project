from django.contrib.auth import get_user_model
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

User = get_user_model()

class UserPayment(models.Model):
	app_user = models.ForeignKey(User, on_delete=models.CASCADE)
	payment_bool = models.BooleanField(default=False)
	stripe_checkout_id = models.CharField(max_length=500)

	class Meta:
		app_label = 'myapp'


@receiver(post_save, sender=User)
def create_user_payment(sender, instance, created, **kwargs):
	if created:
		UserPayment.objects.create(app_user=instance)


