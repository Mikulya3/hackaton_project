from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet

from applications.course.models import Course
from applications.favorite.models import Favorite, Rating, Comment
from applications.favorite.serializers import FavoriteSerializer, RatingSerializer, CommentSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return super().get_queryset()

class RatingViewSet(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]

    def rating(self, request, pk, *args, **kwargs):
        serializer = RatingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        rating_obj, _ = Rating.objects.get_or_create(post_id=pk, owner=request.user)
        rating_obj.rating = request.data['rating']
        rating_obj.save()
        return Response(request.data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        return super().get_queryset()


class FavoriteAPIView(ViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

    @action(detail=False, methods=['get'])
    def list_favorites(self, request):
        if not request.user.is_authenticated:
            return Response([])
        favorites = self.queryset.filter(user=request.user)
        serializer = self.serializer_class(favorites, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def add_favorite(self, request, pk=None):
        course = get_object_or_404(Course, pk=pk)
        favorite, _ = Favorite.objects.get_or_create(user=request.user)
        favorite.course.add(course)
        serializer = self.serializer_class(favorite)
        return Response(serializer.data)

    @action(detail=True, methods=['delete'])
    def remove_favorite(self, request, pk=None):
        course = get_object_or_404(Course, pk=pk)
        favorite = get_object_or_404(Favorite, user=request.user)
        favorite.course.remove(course)
        serializer = self.serializer_class(favorite)
        return Response(serializer.data)

