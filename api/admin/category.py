from django.contrib import admin

from ..models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')
    search_fields = ('name',)
    empty_value_display = '-пусто-'
    prepopulated_fields = {'slug': ('name',)}
