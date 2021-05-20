from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .title import Title
from .user import CustomUser


class Review(models.Model):
    text = models.TextField(
        verbose_name='Отзыв',
        help_text='Введите текст отзыва'
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Произведение',
        help_text='Произведение к которому написан отзыв'
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор',
        help_text='Пользователь который оставил отзыв'
    )
    score = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        verbose_name='Рейтинг',
        help_text='Рейтинг произведения в диапазоне от 1 до 10'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата добавления',
        help_text='Дата и время добавления отзыва'
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ('-pub_date',)

    def __str__(self):
        return self.text
