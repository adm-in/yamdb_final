from rest_framework import viewsets
from rest_framework.generics import get_object_or_404

from ..models import Review, Title
from ..permissions import IsAuthorOrReadOnly
from ..serializers import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    model = Review
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthorOrReadOnly,)

    def get_queryset(self):
        title = get_object_or_404(Title, id=self.kwargs.get('title_id'))
        return title.reviews.all()

    def perform_create(self, serializer):
        title = get_object_or_404(Title, id=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, title=title)
