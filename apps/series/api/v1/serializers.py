from rest_framework import serializers

from apps.series.models import Episodes, Series, EpisodeComment


class EpisodeCommentSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        new_car = EpisodeComment.objects.create(**validated_data)
        return new_car

    class Meta:
        model = EpisodeComment
        fields = '__all__'


class EpisodesSerializer(serializers.ModelSerializer):
    episode_comment = EpisodeCommentSerializer(many=True)

    class Meta:
        model = Episodes
        fields = '__all__'


class SeriesSerializer(serializers.ModelSerializer):
    series_episodes = EpisodesSerializer(many=True)

    class Meta:
        model = Series
        fields = ('title', 'series_episodes')
