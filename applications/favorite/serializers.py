from rest_framework import serializers
from applications.favorite.models import  Comment, Rating, Favorite
from applications.course.models import Course


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(required=False)
    class Meta:
        model = Comment
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(min_value=1, max_value=5)
    class Meta:
        model = Rating
        fields = '__all__'

class FavoriteSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    product_name = serializers.ReadOnlyField(source='course.title')
    rating = serializers.ReadOnlyField(source='course.rating')
    num_reviews = serializers.SerializerMethodField()

    class Meta:
        model = Favorite
        fields = ['user', 'course', 'mentor', 'image', 'product_name', 'rating', 'num_reviews']

    def get_image(self, obj):
        return obj.course.image.url

    def get_num_reviews(self, obj):
        return obj.course.comments.count()
