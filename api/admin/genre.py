from django.contrib import admin

from ..models import Genre


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    empty_value_display = '-пусто-'
