from rest_framework import serializers

from ..models import Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ('id',)
        lookup_field = 'slug'
        extra_kwargs = {'url': {'lookup_field': 'slug'}}
        model = Genre
