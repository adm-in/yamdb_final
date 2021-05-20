from django.contrib import admin

from ..models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'text', 'author', 'score', 'pub_date')
    search_fields = ('title', 'text', 'author__username', 'author__email')
    empty_value_display = '-пусто-'
    list_filter = ('pub_date',)
