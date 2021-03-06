from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins, filters
from rest_framework.permissions import AllowAny

from apps.series.models import Series, Episodes, EpisodeComment
from .serializers import (
    SeriesSerializer,
    EpisodesSerializer,
    EpisodeCommentSerializer,
)


class SeriesAPIView(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin):
    """
        Get Series objects
    """
    permission_classes = [AllowAny, ]
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    http_method_names = ['get', ]


class EpisodesAPIView(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin):
    """
        Get Episodes objects
    """
    permission_classes = [AllowAny, ]
    queryset = Episodes.objects.all()
    serializer_class = EpisodesSerializer
    http_method_names = ['get', ]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = {'imdbRating': ['gte', 'lte'], 'season': ['gte', 'lte'], }
    search_fields = ['series__title', ]


class EpisodeCommentAPIView(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin,
                            mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    """
        CRUD EpisodeComment
    """
    queryset = EpisodeComment.objects.all()
    serializer_class = EpisodeCommentSerializer
