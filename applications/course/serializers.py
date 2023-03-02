from rest_framework import serializers
from applications.course.models import Category, Course, CourseItem, CourseItemFile


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'


class CourseItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseItem
        fields = '__all__'

class CourseItemFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseItemFile
        fields = '__all__'