from rest_framework import serializers

from ..models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ('id',)
        lookup_field = 'slug'
        extra_kwargs = {'url': {'lookup_field': 'slug'}}
        model = Category
