from django.contrib import admin

from ..models import Title


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'year',
        'description',
        'category',
    )
    search_fields = (
        'genre__name',
        'category__name',
        'year',
    )
    empty_value_display = '-пусто-'
    list_filter = ('category',)
