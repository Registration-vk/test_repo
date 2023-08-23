"""
Generated by 'django-admin startproject' using Django 4.2.2.
"""

import os
from pathlib import Path

from django.urls import reverse_lazy

from config import (
    CONFIG_OBJECT,
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = CONFIG_OBJECT.DEBUG

ALLOWED_HOSTS = [
    "127.0.0.1",
    "0.0.0.0",
    "10.100.100.200",
    "109.201.65.62",
]

CSRF_TRUSTED_ORIGINS = CONFIG_OBJECT.CSRF_TRUSTED_ORIGINS

# "security" filter, allowing Django to know whether it is OK (or not)
# to disclose sensitive information within its requests and Debug information output
INTERNAL_IPS = [
    "127.0.0.1",
    # "0.0.0.0",  # not very reliable
]

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "django_celery_results",
    "mail_templated",

    "auth_block.apps.AuthBlockConfig",
    "shop_projects.apps.ShopProjectsConfig",
    "my_projects.apps.MyProjectsConfig",
]

if DEBUG:
    INSTALLED_APPS.extend(
        ["debug_toolbar"],
    )

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = "pro_platform.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "pro_platform.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = CONFIG_OBJECT.DATABASES_CONFIG_DICT

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

if CONFIG_OBJECT.__name__ == 'DevelopmentConfigLocal':
    STATICFILES_DIRS = (
        BASE_DIR / "static",
    )
else:
    STATIC_ROOT = BASE_DIR / "static"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

####################
# mailing list setup
####################

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

# Production
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = "vlad224vlgu@gmail.com"
EMAIL_HOST_PASSWORD = CONFIG_OBJECT.EMAIL_HOST_PASSWORD
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
# EMAIL_TIMEOUT = None

if DEBUG:
    pass
    EMAIL_HOST_USER = None
    EMAIL_HOST_PASSWORD = None
    EMAIL_TIMEOUT = None

    EMAIL_HOST = CONFIG_OBJECT.EMAIL_HOST
    EMAIL_PORT = 1025
    EMAIL_USE_TLS = False
    EMAIL_USE_SSL = False

EMAIL_ADMIN_ADDRESS = "soren@admin.com"

########
# Celery
########
# Celery Configuration Options
CELERY_TIMEZONE = "Europe/Moscow"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 15 * 60

# backend
CELERY_BROKER_URL = CONFIG_OBJECT.CELERY_BROKER_URL
CELERY_RESULT_BACKEND = 'django-db'
CELERY_CACHE_BACKEND = 'django-cache'

# ignore warning
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True

LOGIN_URL = reverse_lazy('auth_block:login')

# DJANGO_SETTINGS_MODULE=pro_platform.settings

########
# Media
########

# Base url to serve media files
MEDIA_URL = '/media/'

# Path where media is stored
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
