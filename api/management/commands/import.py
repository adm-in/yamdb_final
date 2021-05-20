import csv
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from ...models import Category, Comment, CustomUser, Genre, Review, Title

PATH = {
    'USERS': 'data/users.csv',
    'CATEGORIES': 'data/category.csv',
    'GENRES': 'data/genre.csv',
    'TITLES': 'data/titles.csv',
    'GENRES_TITLE': 'data/genre_title.csv',
    'REVIEWS': 'data/review.csv',
    'COMMENTS': 'data/comments.csv',
}

ENCODING = 'utf-8'


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.users()
        self.categories()
        self.genres()
        self.titles()
        self.reviews()
        self.comments()

    def get_path(self, path):
        return os.path.join(settings.BASE_DIR, path)

    def users(self):
        path = self.get_path(PATH['USERS'])
        with open(path, encoding=ENCODING) as f:
            rows = csv.DictReader(f)
            for row in rows:
                row['bio'] = row.pop('description')
                CustomUser.objects.update_or_create(**row)

    def categories(self):
        path = self.get_path(PATH['CATEGORIES'])
        with open(path, encoding=ENCODING) as f:
            rows = csv.DictReader(f)
            for row in rows:
                Category.objects.update_or_create(**row)

    def genres(self):
        path = self.get_path(PATH['GENRES'])
        with open(path, encoding=ENCODING) as f:
            rows = csv.DictReader(f)
            for row in rows:
                Genre.objects.update_or_create(**row)

    def titles(self):
        relationships = {}

        path = self.get_path(PATH['GENRES_TITLE'])
        with open(path, encoding=ENCODING) as f:
            rows = csv.DictReader(f)
            for row in rows:
                title_id = str(row['title_id'])
                if title_id not in relationships:
                    relationships[title_id] = []
                relationships[title_id].append(row['genre_id'])

        path = self.get_path(PATH['TITLES'])
        with open(path, encoding=ENCODING) as f:
            rows = csv.DictReader(f)
            for row in rows:
                for relationship in relationships[str(row['id'])]:
                    if 'category_id' not in row:
                        row['category_id'] = row.pop('category')
                    update, created = Title.objects.update_or_create(**row)
                    update.genre.add(relationship)

    def reviews(self):
        path = self.get_path(PATH['REVIEWS'])
        with open(path, encoding=ENCODING) as f:
            rows = csv.DictReader(f)
            for row in rows:
                row['author_id'] = row.pop('author')
                Review.objects.update_or_create(**row)

    def comments(self):
        path = self.get_path(PATH['COMMENTS'])
        with open(path, encoding=ENCODING) as f:
            rows = csv.DictReader(f)
            for row in rows:
                row['author_id'] = row.pop('author')
                Comment.objects.update_or_create(**row)
