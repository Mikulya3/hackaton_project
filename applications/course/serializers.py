from rest_framework import serializers
from applications.course.models import Category, Course, CourseItem, CourseItemFile


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    # category = CategorySerializer(read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'lang', 'price', 'sub_category']
class CourseItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseItem
        fields = '__all__'

class CourseItemFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseItemFile
        fields = '__all__'