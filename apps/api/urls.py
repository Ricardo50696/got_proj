from django.conf.urls import include
from django.urls import path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework import routers

from apps.api import views

schema_view = get_schema_view(
    openapi.Info(
        title="Series API",
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

router = routers.DefaultRouter()

# API V1 ROOTS
urlpatterns = [
    # API ROOT
    path('', include(router.urls)),

    # API V1 URLS
    path('v1/', include(("apps.api.v1.urls", 'apps.api.v1'), namespace="v1")),

    # API COMMONS
    path('status/', views.health_check, name='health-check'),
]

# SWAGGER
urlpatterns += [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]
