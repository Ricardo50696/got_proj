from rest_framework import serializers

from apps.series.models import Episodes, Series


class EpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episodes
        fields = '__all__'


class SeriesSerializer(serializers.ModelSerializer):
    series_episodes = EpisodesSerializer(many=True)

    class Meta:
        model = Series
        fields = ('title', 'series_episodes')
