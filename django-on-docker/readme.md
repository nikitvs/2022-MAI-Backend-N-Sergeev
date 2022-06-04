```sh
docker-compose -f docker-compose.prod.yml up -d --build 
```

```sh
docker-compose -f docker-compose.prod.yml logs -f    
```

```sh
docker-compose -f docker-compose.prod.yml exec web python manage.py flush --noinput &&
docker-compose -f docker-compose.prod.yml exec web python manage.py makemigrations --noinput &&
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput &&
docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear &&
docker-compose -f docker-compose.prod.yml exec web python manage.py createsuperuser --noinput   
```


```sh
docker-compose -f docker-compose.prod.yml down -v
```
Зайти под postgres:
sudo -i -u postgres

Команды postgres:
    \? — показать список команд;
    \du — показать список пользователей с привилегиями;
    \l — показать список баз данных;
    \с db_name2 — подключиться к другой базе данных;
    \dt — показать список таблиц;
    \d table_name — показать колонки таблицы;
    \x — переключить режим вывода;
    \q — выход из psql.

Подключение к базе:
psql --host=localhost --user=piuser pidatabase

Зайти в контейнер:
docker exec -ti django-on-docker_db_1 /bin/sh

Файлы postgres:
/var/lib/postgresql/data/

Работа с докером:
docker-compose -f docker-compose.prod.yml exec web python manage.py flush --noinput &&
docker-compose -f docker-compose.prod.yml exec web python manage.py makemigrations --noinput &&
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput &&
docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear &&
docker-compose -f docker-compose.prod.yml exec web python manage.py createsuperuser --noinput   

Удалить текщую сборку:
docker-compose -f docker-compose.prod.yml down -v

Удалить все докеры и хранилища:
docker rm -f $(docker ps -a -q)
docker volume prune

Запуск:
make up
или
python3 manage.py runserver localhost:3535

### Показать
docker-compose.yml, Dockerfile, запуск через Makefile 

Админка:
http://localhost:3535/admin/

Показать статику в sources в инструментах разр.