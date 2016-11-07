"""
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'fk57%ckxe(s$$5p6+!@++l-x*b5q^af2v4%ka2%-)-9v5u@wo)'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.humanize',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'mptt',
    'django_mptt_admin',
    'django_markup',
    'printaura',
    'printful',
    'master',
    'catalog',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}

AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/New_York'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '_static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '_media')

SUIT_CONFIG = {
    'ADMIN_NAME': '559 Labs / eShop Manager',
    'MENU': (
         {
            'label': 'Catalog',
            'icon': 'icon-cog',
            'models': (
                'master.Outlet',
                'master.PODVendor',
                'master.Brand',
                'master.Product',
            ),
         },
         {
             'label': 'Creative',
             'icon': 'icon-cog',
             'models': (
                'master.Artist',
                'master.Creative',
                'master.CreativeSeries',
             ),
         },
         {
            'label': 'Metadata',
            'icon': 'icon-cog',
            'models': (
                'master.Category',
                'master.GoogleCategory',
                'master.Color',
                'master.Size',
                'master.Variant',
            ),
         },
         {
            'label': 'Vendor Catalogs',
            'icon': 'icon-cog',
            'models': (
                'master.VendorProduct',
                'master.VendorVariant',
                'master.VendorCategory',
                'master.VendorBrand',
                'master.VendorColor',
                'master.VendorSize',
            ),
          },
         {
             'label': 'Catalog',
             'icon': 'icon-cog',
             'app': 'catalog',
         },
         {
             'label': 'Security',
             'icon': 'icon-cog',
             'app': 'auth',
          },
    )
}

from .local_settings import *
