from django.contrib import admin
from applications.course.models import Category, Course, CourseItem, CourseItemFile

admin.site.register(Category)
admin.site.register(Course)
admin.site.register(CourseItem)
admin.site.register(CourseItemFile)


