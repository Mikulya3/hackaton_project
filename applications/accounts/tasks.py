import time
from django.core.mail import send_mail
from main.celery import app

@app.task
def send_confirmation_code(email, code):
    time.sleep(1)
    full_link = f'http://localhost:8000/accounts/activate/{code}'
    send_mail(
        'Восстановление пароля',
        full_link,
        'Kadirbekova43@gmail.com',
        [email]
    )