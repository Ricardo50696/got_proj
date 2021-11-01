from django_filters import filters, FilterSet

from apps.series.models import Series


class SeriesFilter(FilterSet):
    imdbRating = filters.Filter(field_name='series_episodes__imdbRating')

    class Meta:
        model = Series
        fields = ['imdbRating', ]
