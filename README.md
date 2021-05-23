# Проект: YaMDb
![workflow](https://github.com/adm-in/yamdb_final/actions/workflows/yamdb_workflow.yaml/badge.svg)
# Описание проекта:
Проект YaMDb собирает отзывы (Review) пользователей на произведения (Title). Произведения делятся на категории: «Книги», «Фильмы», «Музыка». Список категорий (Category) может быть расширен (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»).

# Команды для запуска приложения:
1. Устанавливаем docker командой sudo apt install ```sudo apt install docker.io ``` .
2. Устанавливаем docker-compose используя [официальную](https://docs.docker.com/compose/install/) документацию.
3. Клонируем репозиторий ```https://github.com/adm-in/yamdb_final``` и переходим в него.
3. Далее собираем образ и запускаем docker-compose командой ```docker-compose up -d --build```.
4. Зайдите на http://127.0.0.1/admin/ и убедитесь, что страница отображается полностью: статика подгрузилась и вы можете залогиниться под суперпользователем которого только что создали. 

- [admin](http://djangoproject.gq/admin)
- [api](http://djangoproject.gq/api/v1)
- [redoc](http://djangoproject.gq/redoc)

### Технологии:
- [Django 3.0.5](https://www.djangoproject.com)
- [DjangoRestFramework 3.11.0](https://www.django-rest-framework.org)
- [Docker 20.10.6](https://www.docker.com)
- [Gunicorn 20.0.4](https://gunicorn.org)
- [Postgres 12.4](https://www.postgresql.org)
- [Python 3.8](https://www.python.org)
- [PyJWT 1.7.1](https://pyjwt.readthedocs.io/en/stable)
- [Nginx 1.19.3](https://nginx.org)

### Проект разработан: 
https://github.com/adm-in/
- [Licensed under the Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)