from .category import CategoryViewSet
from .comment import CommentViewSet
from .genre import GenreViewSet
from .review import ReviewViewSet
from .title import TitleViewSet
from .user import AuthViewSet, TokenViewSet, UserViewSet

__all__ = [
    'CategoryViewSet',
    'CommentViewSet',
    'GenreViewSet',
    'ReviewViewSet',
    'TitleViewSet',
    'AuthViewSet',
    'TokenViewSet',
    'UserViewSet',
]
