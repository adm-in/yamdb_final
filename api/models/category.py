from django.db import models


class Category(models.Model):
    name = models.CharField(
        verbose_name='Наименование',
        db_index=True,
        max_length=255
    )
    slug = models.SlugField(
        verbose_name='Слаг',
        unique=True,
        db_index=True,
        max_length=255
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)

    def __str__(self):
        return self.name
