from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from applications.course.models import Course
from main import settings
from django.db.models import Avg


User = get_user_model()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()

    def __str__(self):
        return f'{self.course}-{self.comment}'

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rating')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='ratings')
    rating = models.SmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ],
        blank=True, null=True
    )

    def __str__(self):
        return f'{self.course} - {self.rating} '


class Favorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='favorites')
    mentor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='mentors', limit_choices_to={'is_mentor': True})

    def __str__(self):
        return f'{self.user} - {self.course.title}'

    @property
    def image(self):
        return self.course.image.url

    @property
    def product_name(self):
        return self.course.title

    def get_rating(self):
        ratings = self.course.ratings.aggregate(avg_rating=Avg('rating'))
        return ratings['avg_rating'] if ratings['avg_rating'] else 0

    def get_num_reviews(self):
        return self.course.comments.count()
