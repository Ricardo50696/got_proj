from django.contrib.gis.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

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

    def changeform_link(self):
        if self.id:
            changeform_url = reverse(
                'admin:series_episodes_change', args=(self.id,)
            )
            return mark_safe(u'<a href="%s" target="_blank">Details</a>' % changeform_url)
        return u''
    changeform_link.allow_tags = True
    changeform_link.short_description = ''


class EpisodeComment(models.Model):
    comment = models.TextField(_('Comment'), null=True, blank=True)
    episode = models.ForeignKey(Episodes, related_name='episode_comment', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Episode Comment')
        verbose_name_plural = _('Episode Comment')

    def __str__(self):
        return f'{self.comment}'
