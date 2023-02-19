import time
from django.core.mail import send_mail

from main.celery import app


def send_confirmation_email(email, code):
    full_link = f'http://localhost:8000/account/activate/{code}'
    send_mail(
        'Активация пользователя',
        full_link,
        'Kadirbekova43@gmail.com',
        [email]
    )


def send_confirmation_code(email, code):
    send_mail(
        'Восстановление пароля',
        code,
        'Kadirbekova43@gmail.com',
        [email]
    )

@app.task
def send_confirmation_code_celery(email, code):
    time.sleep(1)
    full_link = f'http://localhost:8000/accounts/activate/{code}'
    send_mail(
        'Восстановление пароля',
        full_link,
        'Kadirbekova43@gmail.com',
        [email]
    )