import environ

from .base import *

env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env(str(BASE_DIR / ".env.prod"))

SECRET_KEY = env.str("SECRET_KEY")
DEBUG = env.bool("DEBUG")

ALLOWED_HOSTS = ["mini-django-railway-production.up.railway.app"]
CSRF_TRUSTED_ORIGINS = [
    "https://mini-django-railway-production.up.railway.app"
]  # modify later

MIDDLEWARE = MIDDLEWARE + ["whitenoise.middleware.WhiteNoiseMiddleware"]

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql_psycopg2",
#         "NAME": env.str("DB_NAME"),
#         "USER": env.str("DB_USER"),
#         "PASSWORD": env.str("DB_PWD"),
#         "HOST": env.str("DB_HOST"),
#         "PORT": env.str("DB_PORT"),
#     }
# }

# If you want to use sqlite3 instead, then uncomment this and comment the above.

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

STATIC_ROOT = str(BASE_DIR / "staticfiles")
STATICFILES_DIRS = (str(BASE_DIR / "static"),)

# Connect to our database remotely
import dj_database_url

DATABASE_URL = env.str("DATABASE_URL")

DATABASES = {"default": dj_database_url.config(default=DATABASE_URL)}
