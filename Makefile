dev-start:
	python3 manage.py runserver --settings=config.settings.dev
dev-migrate:
	python3 manage.py migrate --settings=config.settings.dev
dev-makemigrations:
	python3 manage.py makemigrations --settings=config.settings.dev
dev-shell:
	python3 manage.py shell --settings=config.settings.dev
dev-shell-plus:
	python3 manage.py shell_plus --settings=config.settings.dev
dev-install:
	pip install -r requirements/dev.txt
dev-test:
	python3 manage.py test --settings=config.settings.dev

prod-install:
	pip install -r requirements/prod.txt
prod-migrate:
	python3 manage.py migrate --settings=config.settings.prod
prod-superuser:
	python3 manage.py createsuperuser --settings=config.settings.prod
prod-collectstatic:
	python3 manage.py collectstatic --settings=config.settings.prod
prod-gunicorn:
	gunicorn config.wsgi --env DJANGO_SETTINGS_MODULE=config.settings.prod