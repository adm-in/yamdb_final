from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from ..models import Review


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        fields = ('id', 'text', 'author', 'score', 'pub_date')
        model = Review

    def validate(self, data):
        if not self.instance:
            title_id = self.context.get('view').kwargs.get('title_id')
            user = self.context.get('request').user
            if Review.objects.filter(author=user, title_id=title_id).exists():
                raise ValidationError(
                    'Вы уже оставили отзыв на это произведение.'
                )
        return data
