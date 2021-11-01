from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _


class Series(models.Model):
    title = models.CharField(_('Title'), max_length=100)

    class Meta:
        verbose_name = _('Series')
        verbose_name_plural = _('Series')

    def __str__(self):
        return f'{self.title}'


class Episodes(models.Model):
    title = models.CharField(_('Title'), max_length=100)
    season = models.CharField(_('Season'), max_length=100, blank=True, null=True)
    episode_number = models.IntegerField(_('Episode number'), blank=True, null=True)
    released = models.DateField(_('Released'), blank=True, null=True)
    imdbRating = models.DecimalField(_('imdb Rating'), decimal_places=1, max_digits=3, blank=True, null=True)
    series = models.ForeignKey(Series, related_name='series_episodes', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Episode')
        verbose_name_plural = _('Episodes')
        ordering = ['season', 'episode_number']

    def __str__(self):
        return f'{self.title}'
