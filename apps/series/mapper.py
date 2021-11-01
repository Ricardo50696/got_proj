from apps.series.models import Episodes
import re


class OMDBApiMapper:
    """
    Custom Mapper for OMDB API.
    """

    def api_to_class_episodes(self, api_obj, series):
        """
        Converts an API object into a dictionary object using Episodes fields as keys.
        Creates and saves Episodes from API object
        """
        series_episodes = []
        for episode in api_obj['Episodes']:
            episode_obj = dict(
                title=episode['Title'],
                season=api_obj['Season'],
                episode_number=episode['Episode'],
                released=episode['Released'],
                imdbRating=episode['imdbRating'] if re.match(r'^-?\d+(?:\.\d+)$', episode['imdbRating']) else None,
                series=series,
            )
            series_episodes.append(Episodes(**episode_obj))
        Episodes.objects.bulk_create(series_episodes)
