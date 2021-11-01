from django.contrib import admin

from .models import Series, Episodes


class EpisodesInlineAdmin(admin.TabularInline):
    model = Episodes
    ordering = ('season', 'episode_number', )
    extra = 1


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    inlines = [EpisodesInlineAdmin, ]
