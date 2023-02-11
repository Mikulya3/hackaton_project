# Generated by Django 4.1.6 on 2023-02-09 07:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_customuser_activation_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classroom',
            name='status',
        ),
        migrations.RemoveField(
            model_name='teaching',
            name='status',
        ),
        migrations.AddField(
            model_name='classroom',
            name='question',
            field=models.CharField(default=True, max_length=500),
        ),
        migrations.AddField(
            model_name='classroom',
            name='user',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='teaching',
            name='question',
            field=models.CharField(default=True, max_length=500),
        ),
        migrations.AddField(
            model_name='teaching',
            name='user',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='answer',
            field=models.CharField(blank=True, choices=[('1', 'в настоящий момент нет'), ('2', 'у меня маленькая аудитория'), ('3', 'у меня достаточная аудитория')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='teaching',
            name='answer',
            field=models.CharField(blank=True, choices=[('1', 'лично, частным образом'), ('2', 'лично, профессионально'), ('3', 'онлайн'), ('4', 'другое')], max_length=50, null=True),
        ),
    ]
