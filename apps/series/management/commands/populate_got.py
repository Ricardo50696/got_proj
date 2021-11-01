import requests
from django.core.management.base import BaseCommand

from apps.series.mapper import OMDBApiMapper
from apps.series.models import Series


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # TODO replace apiKey to env file
        url = 'http://www.omdbapi.com/?t=Game%20of%20Thrones&Season=1&apikey=685583ba'
        response = requests.get(url)
        total_seasons = response.json()['totalSeasons']
        series = Series(title=response.json()['Title'])
        series.save()
        for season in range(1, int(total_seasons)):
            url = 'http://www.omdbapi.com/?t=Game%20of%20Thrones&Season={}&apikey=685583ba'.format(season)
            response = requests.get(url)
            mapper = OMDBApiMapper()
            mapper.api_to_class_episodes(response.json(), series)
