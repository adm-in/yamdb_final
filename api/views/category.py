from rest_framework.filters import SearchFilter

from ..mixins import ListAndCreateAndDestoryViewSet
from ..models import Category
from ..permissions import IsAdmin, ReadOnly
from ..serializers import CategorySerializer


class CategoryViewSet(ListAndCreateAndDestoryViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
    permission_classes = [ReadOnly | IsAdmin]
    filter_backends = (SearchFilter,)
    search_fields = ('name',)
