from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryAPIView, CourseAPIView, CourseItemAPIView, CourseItemFileAPIView

router = DefaultRouter()
router.register('category', CategoryAPIView)
router.register('courseitem', CourseItemAPIView)
router.register('courseitemfile', CourseItemFileAPIView)
router.register('', CourseAPIView)


urlpatterns = [

    path('', include(router.urls)),

]
