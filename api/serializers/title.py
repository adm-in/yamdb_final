from rest_framework import serializers

from ..models import Category, Genre, Title
from .category import CategorySerializer
from .genre import GenreSerializer


class TitleCreateUpdateSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='slug'
    )
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        slug_field='slug',
        many=True
    )

    class Meta:
        fields = (
            'id',
            'name',
            'year',
            'category',
            'genre',
            'description',
        )
        model = Title


class TitleListSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True)
    category = CategorySerializer()
    rating = serializers.FloatField()

    class Meta:
        fields = (
            'id',
            'name',
            'year',
            'category',
            'genre',
            'rating',
            'description',
        )
        model = Title
