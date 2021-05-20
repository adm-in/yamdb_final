from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'api'

router_v1 = DefaultRouter()

router_v1.register(
    r'users',
    views.UserViewSet,
    basename='users'
)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    views.CommentViewSet,
    basename='comments',
)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews',
    views.ReviewViewSet,
    basename='reviews',
)
router_v1.register(
    r'categories',
    views.CategoryViewSet,
    basename='categories'
)
router_v1.register(
    r'genres',
    views.GenreViewSet,
    basename='genres'
)
router_v1.register(
    r'titles',
    views.TitleViewSet,
    basename='titles'
)

urlpatterns = [
    path('v1/auth/token/', views.TokenViewSet.as_view(), name='token'),
    path('v1/auth/email/', views.AuthViewSet.as_view(), name='auth'),
    path('v1/', include(router_v1.urls)),
]
