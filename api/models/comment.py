from django.db import models

from .review import Review
from .user import CustomUser


class Comment(models.Model):
    text = models.TextField(
        verbose_name='Комментарий',
        help_text='Введите текст комментария',
    )
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Отзыв',
        help_text='Отзыв к которому оставлен комментарий',
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор',
        help_text='Пользователь который оставил комментарий',
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата добавления',
        help_text='Дата и время добавления комментария',
    )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('-pub_date',)

    def __str__(self):
        return self.text
