"""
GOT admin URL Configuration
"""
from django.contrib import admin
from django.urls import path

admin.site.site_header = "Game of Thrones Administration"
admin.site.site_title = "Admin"
admin.site.index_title = "GOT"

urlpatterns = [
    path('admin/', admin.site.urls),
]