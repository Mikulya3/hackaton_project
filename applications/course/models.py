from django.conf.global_settings import LANGUAGES
from enumfields import EnumField
from enum import Enum
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Category(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

LANGUAGES = [
    ('aa', 'Afar'),
    ('ab', 'Abkhazian'),
    ('ae', 'Avestan'),
    ('kg', 'Kyrgyzstan'),
    ('eng', 'English'),
    ('rus', 'Russian'),

    # and so on, for all the languages of the world...
]

class Level(Enum):
    BEGGINING = 'BG'
    MIDDLE = 'MD'
    PROFESSIONAL = 'PR'
    ALL = 'ALL'


class Course(models.Model):
    id = models.AutoField(primary_key=True, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=60, blank=True, null=True)
    sub_title = models.CharField(max_length=60, blank=True, null=True)
    description = models.TextField(max_length=200, blank=True, null=True)
    lang = models.CharField(max_length=3, choices=LANGUAGES)
    level = models.CharField(max_length=3, choices=[(level.value, level.name) for level in Level])
    sub_category = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='image/')
    video = models.FileField(upload_to='video/', blank=False, null=True)
    price = models.DecimalField(max_digits=19, decimal_places=10, default=0)
    currency = models.CharField(max_length=3, default='USD')

    def __str__(self):
        return self.title
class CourseItem(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, null=True,blank=True)
    description = models.TextField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.title, self.description

class CourseItemFile(models.Model):
    courseitem_id = models.ForeignKey(CourseItem, on_delete=models.CASCADE)
    video_file = models.FileField(upload_to='lectures/videos', null=True, blank=True)
    link = models.URLField(null=True, blank=True)





