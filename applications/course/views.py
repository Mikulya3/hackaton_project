from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from applications.course.models import Category, Course, CourseItem, CourseItemFile
from applications.course.serializers import CategorySerializer, CourseSerializer, CourseItemSerializer, CourseItemFileSerializer


class CategoryAPIView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['title']
    search_fields = ['title']

class CourseAPIView(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend,  filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['title', 'sub_category']
    search_fields = ['title']
    ordering_fields = ['title', 'lang', 'price', 'description']

class CourseItemAPIView(ModelViewSet):
    queryset = CourseItem.objects.all()
    serializer_class = CourseItemSerializer

class CourseItemFileAPIView(ModelViewSet):
    queryset = CourseItemFile.objects.all()
    serializer_class = CourseItemFileSerializer
