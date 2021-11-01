from rest_framework import routers

from apps.series.api.v1.views import (
    SeriesAPIView,
    EpisodesAPIView,
)

router = routers.SimpleRouter()
router.register(r'series', SeriesAPIView, basename='series')
router.register(r'episodes', EpisodesAPIView, basename='episodes')
app_name = 'series'

urlpatterns = [
              ] + router.urls
