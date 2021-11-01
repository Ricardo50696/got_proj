from rest_framework import routers

from apps.series.api.v1.views import (
    SeriesAPIView,
    EpisodesAPIView,
    EpisodeCommentAPIView,
)

router = routers.SimpleRouter()
router.register(r'series', SeriesAPIView, basename='series')
router.register(r'episodes', EpisodesAPIView, basename='episodes')
router.register(r'episode-comments', EpisodeCommentAPIView, basename='episode-comments')
app_name = 'series'

urlpatterns = [
              ] + router.urls
