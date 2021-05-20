from django.utils import timezone
from django.utils.crypto import get_random_string
from rest_framework import serializers

from ..models import ConfirmationCode, CustomUser


class ConfirmationCodeOutsetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfirmationCode
        fields = ('email',)

    def create(self, validated_data):
        validated_data['confirmation_code'] = get_random_string(
            length=ConfirmationCode.CONFIRMATION_CODE_MAX_LENGTH
        )
        validated_data['expiry_date'] = (
            timezone.now() + ConfirmationCode.CONFIRMATION_CODE_LIFETIME
        )

        item = super().create(validated_data)
        item.send()

        return item


class ConfirmationCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()

    confirmation_code = serializers.CharField(
        max_length=ConfirmationCode.CONFIRMATION_CODE_MAX_LENGTH
    )


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'first_name',
            'last_name',
            'username',
            'bio',
            'email',
            'role',
        )
        model = CustomUser
