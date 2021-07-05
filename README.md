### Инфо
Чистый python проект с docker + django + nginx + gunicorn + postgresql

Просто запустить команды ниже для запуска проекта

### Сборка
docker-compose build

### Запуск
docker-compose up -d

### Остановка
docker-compose down

### Войти в Docker по ssh
docker exec -it third-project-docker_python_1 /bin/bash

#### Миграции
python3 manage.py makemigrations

python3 manage.py migrate

#### Установка thumblains для проекта
pip install sorl-thumbnail

python manage.py migrate

в шаблоне:
`
{% load thumbnail %}
{% thumbnail image.image "300" as im %}
    <a href="{{ image.image.url }}">
        <img src="{{ im.url }}" class="image-detail">
    </a>
{% endthumbnail %}

источник https://pocoz.gitbooks.io/django-v-primerah/content/glava-5-obschii-dostup-k-kontentu-na-saite/sozdanie-miniatyur-izobrazhenii-s-pomoschyu-sorl-thumbnail.html
`


### Источник
https://www.haikson.com/programmirovanie/python/django-nginx-gunicorn-postgresql-docker/ 

https://rtfm.co.ua/django-net-fajlov-css-js-i-drugix-statichnyx-fajlov/