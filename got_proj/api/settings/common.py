from got_proj.settings import *

INSTALLED_APPS += [

    # Third-Party Integrations
    'rest_framework',
    'drf_yasg',
    'django_filters',

]

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 20
}