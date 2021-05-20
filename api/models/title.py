from django.db import models

from ..validators import year_validator
from .category import Category
from .genre import Genre


class Title(models.Model):
    year = models.PositiveSmallIntegerField(
        validators=(year_validator,),
        verbose_name='Год выпуска',
    )
    name = models.CharField(
        verbose_name='Наименование',
        max_length=255,
        db_index=True
    )
    description = models.TextField(
        verbose_name='Описание',
        null=True
    )
    genre = models.ManyToManyField(
        Genre,
        verbose_name='Жанр',
        related_name='titles'
    )
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        on_delete=models.SET_NULL,
        null=True,
        related_name='titles',
    )

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'
        ordering = ('year',)

    def __str__(self):
        return self.name
