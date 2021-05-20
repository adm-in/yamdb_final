from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from ..forms import CustomUserChangeForm, CustomUserCreationForm
from ..models import ConfirmationCode, CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    list_display = ('email', 'is_staff', 'is_active', 'role')
    list_filter = ('is_staff', 'is_active', 'role')

    fieldsets = (
        (None, {
            'fields': (
                'email',
                'username',
                'first_name',
                'last_name',
                'password',
                'bio',
                'role'
            )
        }),
        ('Permissions', {
            'fields': (
                'is_staff',
                'is_active'
            )
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': (
                'wide',
            ),
            'fields': (
                'email',
                'username',
                'first_name',
                'last_name',
                'password1',
                'password2',
                'bio',
                'role',
                'is_staff',
                'is_active'
            )
        }),
    )

    search_fields = ('email',)
    ordering = ('email',)


@admin.register(ConfirmationCode)
class ConfirmationCodeAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'email',
        'confirmation_code',
        'is_used',
        'expiry_date',
    )
    search_fields = (
        'email',
        'confirmation_code',
    )
    list_filter = (
        'expiry_date',
    )
    empty_value_display = '-пусто-'
