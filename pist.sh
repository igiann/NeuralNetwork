git clone git@github.com:django-cms/django-cms-quickstart.git
cd django-cms-quickstart
docker compose build web && docker compose up -d database_default
docker compose run web python manage.py migrate && docker compose run web python manage.py createsuperuser
docker compose up -d
open http://127.0.0.1:8000
