from rest_framework import viewsets, filters, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CourseItemAPIView(ModelViewSet):
    queryset = CourseItem.objects.all()
    serializer_class = CourseItemSerializer

class CourseItemFileAPIView(ModelViewSet):
    queryset = CourseItemFile.objects.all()
    serializer_class = CourseItemFileSerializer
