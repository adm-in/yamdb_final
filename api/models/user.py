from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models

from ..managers import CustomUserManager


class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        USER = 'user', 'Пользователь'
        MODERATOR = 'moderator', 'Модератор'
        ADMIN = 'admin', 'Администратор'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    email = models.EmailField(
        verbose_name='Адрес электронной почты',
        unique=True
    )
    bio = models.TextField(
        verbose_name='О себе',
        null=True,
        blank=True
    )
    role = models.CharField(
        verbose_name='Роль',
        max_length=9,
        default=Role.USER,
        choices=Role.choices
    )

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('-id',)

    def __str__(self):
        return self.email

    @property
    def is_user(self):
        return str(self.role) == self.Role.USER

    @property
    def is_moderator(self):
        return str(self.role) == self.Role.MODERATOR

    @property
    def is_admin(self):
        return str(self.role) == self.Role.ADMIN

    def to_appoint_an_administrator(self):
        self.is_staff = True
        self.is_superuser = True
        self.is_active = True
        self.role = self.Role.ADMIN


class ConfirmationCode(models.Model):
    CONFIRMATION_CODE_LIFETIME = settings.CONFIRMATION_CODE_LIFETIME
    CONFIRMATION_CODE_MAX_LENGTH = 62

    email = models.EmailField(
        verbose_name='Адрес электронной почты'
    )
    confirmation_code = models.CharField(
        verbose_name='Код подтверждения',
        max_length=CONFIRMATION_CODE_MAX_LENGTH
    )
    is_used = models.BooleanField(
        verbose_name='Использован ли код подтверждения',
        default=False
    )
    expiry_date = models.DateTimeField(
        verbose_name='Дата истечения срока действия',
        blank=True
    )

    class Meta:
        verbose_name = 'Код подтверждения'
        verbose_name_plural = 'Коды подтверждения'

        constraints = (
            models.UniqueConstraint(
                fields=('email', 'confirmation_code'), name='unique_code'
            ),
        )

    def __str__(self):
        return self.email

    def send(self):
        subject = 'Код подтверждения'
        message = f'Ваш код подтверждения: {self.confirmation_code}'

        from_e = settings.EMAIL_HOST_USER
        to_e = (self.email,)

        send_mail(subject, message, from_e, [to_e])
