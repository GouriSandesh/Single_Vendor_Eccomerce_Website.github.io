"""
Django settings for ecoProject project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os.path
from pathlib import Path

from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-wxa%9!zq#()&!_^us14z*1^-)0z!iq5-qs27_nfb&)8@xi10dp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['.vercel.app']

LOGIN_URL = "/loginpage"



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ecoApp',
    'crispy_forms',
    'crispy_bootstrap5',
    "django_icons",
    "channels",
    "widget_tweaks"
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'ecoApp.middleware.TrafficMiddleware',
]

ROOT_URLCONF = 'ecoProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ecoProject.wsgi.application'
ASGI_APPLICATION = 'ecoProject.asgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'ecoApp.User'

CRISPY_ALLOWED_TEMPLATE_PACKS='bootstrap5'
CRISPY_TEMPLATE_PACK='bootstrap5'


MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR,"media")

CART_SESSION_ID = 'cart'

DJANGO_ICONS = {
    "ICONS": {
        "edit": {"name": "fa-solid fa-pen-to-square"},
        "del": {"name": "fa-solid fa-trash"},
        "close": {"name": "fa-solid fa-circle-xmark"},
        "heart": {"name":"fa-solid fa-heart"}
    }
}

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

STRIPE_PUBLISHABLE_KEY = 'pk_test_51QgsiXIRVYJPai1OiaCm2kyMYaXsALdrSFsHSmNaOlrwDxBPhhTgpQILa5P0gMtWCtU7KmtXgvrcA0AtsFvy6e6o00V6KUDJRs'
STRIPE_SECRET_KEY = 'sk_test_51QgsiXIRVYJPai1OJeREo8VNpMxA8PBzeIii5UALMW4u0421ebbFLTa7qm1UCQ8fGDkBlb1kwKtdYEWZnQwhbFL900cCDmkZbK'


BACKEND_DOMAIN = 'http://localhost:8000'  # or your production domain
PAYMENT_SUCCESS_URL = 'http://localhost:8000/SuccessView'
PAYMENT_CANCEL_URL =  'http://localhost:8000/CancelView'

