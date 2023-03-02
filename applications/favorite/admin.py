from django.contrib import admin
from applications.favorite.models import Favorite, Rating, Comment
from django.urls import reverse
from django.utils.html import format_html
from applications.course.models import Course

class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('mentor', 'get_price', 'get_image', 'get_rating', 'get_num_reviews')


    def get_price(self, obj):
        return obj.course.price

    get_price.short_description = "Price"

    def get_image(self, obj):
        return obj.course.image.url if obj.course.image else ''

    get_image.short_description = "Course Image"

    def get_rating(self, obj):
        return obj.get_rating()

    get_rating.short_description = "Course Rating"

    def get_num_reviews(self, obj):
        return obj.get_num_reviews()

    get_num_reviews.short_description = "Number of comments"

admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(Comment)
admin.site.register(Rating)


