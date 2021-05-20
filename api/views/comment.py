from rest_framework import viewsets
from rest_framework.generics import get_object_or_404

from ..models import Comment, Review
from ..permissions import IsAuthorOrReadOnly
from ..serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    model = Comment
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly,)

    def get_queryset(self):
        review = get_object_or_404(
            Review,
            title_id=self.kwargs.get('title_id'),
            id=self.kwargs.get('review_id'),
        )
        return review.comments.all()

    def perform_create(self, serializer):
        review = get_object_or_404(
            Review,
            title_id=self.kwargs.get('title_id'),
            id=self.kwargs.get('review_id'),
        )
        serializer.save(author=self.request.user, review=review)
