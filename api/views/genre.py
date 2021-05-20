from rest_framework.filters import SearchFilter

from ..mixins import ListAndCreateAndDestoryViewSet
from ..models import Genre
from ..permissions import IsAdmin, ReadOnly
from ..serializers import GenreSerializer


class GenreViewSet(ListAndCreateAndDestoryViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    lookup_field = 'slug'
    permission_classes = [ReadOnly | IsAdmin]
    filter_backends = (SearchFilter,)
    search_fields = ('name',)
