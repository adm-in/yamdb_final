from django.utils import timezone
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from ..models import ConfirmationCode, CustomUser
from ..permissions import IsAdmin
from ..serializers import (ConfirmationCodeOutsetSerializer,
                           ConfirmationCodeSerializer, CustomUserSerializer)


class TokenViewSet(APIView):
    http_method_names = ('post',)

    def post(self, request, *args, **kwargs):
        serializer = ConfirmationCodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            validated_data = serializer.validated_data

            confirmation_code = ConfirmationCode.objects.get(
                email=validated_data['email'],
                confirmation_code=validated_data['confirmation_code'],
                is_used=False,
                expiry_date__gte=timezone.now(),
            )
        except ConfirmationCode.DoesNotExist:
            return Response(
                {
                    'confirmation_code': (
                        'Недействительный код подтверждения.',
                    )
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )

        confirmation_code.is_used = True
        confirmation_code.save()

        user, created = CustomUser.objects.get_or_create(
            email=confirmation_code.email)
        refresh = RefreshToken.for_user(user)

        return Response(
            {'token': str(refresh.access_token)},
            status=status.HTTP_201_CREATED,
        )


class AuthViewSet(APIView):
    http_method_names = ('post',)

    def post(self, request, *args, **kwargs):
        serializer = ConfirmationCodeOutsetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = (IsAuthenticated, IsAdmin)
    lookup_field = 'username'
    filter_backends = (SearchFilter,)
    search_fields = ('username',)

    @action(
        detail=False,
        methods=('get', 'patch'),
        permission_classes=(IsAuthenticated,),
    )
    def me(self, request, *args, **kwargs):
        if request.method == 'PATCH':
            serializer = self.get_serializer(
                request.user, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        else:
            serializer = self.get_serializer(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)
