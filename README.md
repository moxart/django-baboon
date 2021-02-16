## Usage

#### Development
```
$ docker-compose up -d --build
$ docker-compose exec web python manage.py flush
$ docker-compose exec web python manage.py makemigrations
$ docker-compose exec web python manage.py migrate
$ docker-compose exec web python manage.py createsuperuser
```

#### Production
```
$ docker-compose down -v
$ docker volume create --name=db_data
$ docker volume create --name=static_volume
$ docker volume create --name=media_volume
$ docker-compose -f docker-compose.prod.yml up -d --build
$ docker-compose -f docker-compose.prod.yml exec web python manage.py migrate
$ docker-compose -f docker-compose.prod.yml exec web python manage.py createsuperuser
$ docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input
```