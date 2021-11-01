from .common import *

PREPEND_WWW = False
DEBUG = True

PROJECT_URL = 'http://0.0.0.0:8000'
ALLOWED_HOSTS = ['*', ]

INSTALLED_APPS += (
    'django_extensions',
)

ROOT_URLCONF = 'got_proj.api.urls'
