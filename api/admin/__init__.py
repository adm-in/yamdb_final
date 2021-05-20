from .category import CategoryAdmin
from .comment import CommentAdmin
from .genre import GenreAdmin
from .review import ReviewAdmin
from .title import TitleAdmin
from .user import ConfirmationCodeAdmin, CustomUserAdmin

__all__ = [
    'CategoryAdmin',
    'CommentAdmin',
    'GenreAdmin',
    'ReviewAdmin',
    'TitleAdmin',
    'ConfirmationCodeAdmin',
    'CustomUserAdmin',
]
