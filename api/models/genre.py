from django.db import models


class Genre(models.Model):
    name = models.CharField(
        verbose_name='Наименование',
        max_length=255,
        db_index=True
    )
    slug = models.SlugField(
        verbose_name='Слаг',
        unique=True,
        max_length=255,
        db_index=True
    )

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ('name',)

    def __str__(self):
        return self.name
