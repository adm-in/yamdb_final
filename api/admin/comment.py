from django.contrib import admin

from ..models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'review', 'author', 'pub_date')
    search_fields = ('text', 'author__username', 'author__email')
    empty_value_display = '-пусто-'
    list_filter = ('pub_date',)
