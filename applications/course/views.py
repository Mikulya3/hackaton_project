from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from applications.course.models import Category, Course, CourseItem, CourseItemFile
from applications.course.serializers import CategorySerializer, CourseSerializer, CourseItemSerializer, \
    CourseItemFileSerializer


class CategoryAPIView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CourseAPIView(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseItemAPIView(ModelViewSet):
    queryset = CourseItem.objects.all()
    serializer_class = CourseItemSerializer

class CourseItemFileAPIView(ModelViewSet):
    queryset = CourseItemFile.objects.all()
    serializer_class = CourseItemFileSerializer
