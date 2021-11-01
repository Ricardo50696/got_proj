from django.contrib import admin

from .models import Series, Episodes, EpisodeComment


class EpisodeCommentInlineAdmin(admin.TabularInline):
    model = EpisodeComment
    extra = 1


@admin.register(Episodes)
class EpisodesAdmin(admin.ModelAdmin):
    inlines = [EpisodeCommentInlineAdmin, ]


class EpisodesLinkInline(admin.TabularInline):
    model = Episodes
    fields = ('season', 'episode_number', 'released', 'imdbRating',  'changeform_link')
    readonly_fields = ('changeform_link',)


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    inlines = [EpisodesLinkInline, ]
