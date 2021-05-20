from django.db.models import Avg
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import SAFE_METHODS

from ..filters import TitleFilter
from ..models import Title
from ..permissions import IsAdmin, ReadOnly
from ..serializers import TitleCreateUpdateSerializer, TitleListSerializer


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.annotate(
        rating=Avg('reviews__score')).order_by('year')
    filter_backends = [DjangoFilterBackend]
    filterset_class = TitleFilter
    permission_classes = [ReadOnly | IsAdmin]

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return TitleListSerializer
        return TitleCreateUpdateSerializer
