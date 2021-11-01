from django.conf.urls import include
from django.urls import path
from rest_framework import routers

router = routers.DefaultRouter()

# All API V1 URLS
urlpatterns = [
    # V1 API ROOT
    path('', include(router.urls)),
    path('', include('apps.series.api.v1.urls')),

]
