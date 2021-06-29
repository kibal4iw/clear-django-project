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

### Источник
https://www.haikson.com/programmirovanie/python/django-nginx-gunicorn-postgresql-docker/ 

https://rtfm.co.ua/django-net-fajlov-css-js-i-drugix-statichnyx-fajlov/