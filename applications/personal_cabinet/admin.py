from django.contrib import admin

from applications.personal_cabinet.models import UserProfile, MentorProfile

admin.site.register(UserProfile)
admin.site.register(MentorProfile)


