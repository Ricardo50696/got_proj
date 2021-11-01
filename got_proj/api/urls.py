"""
got_proj api URL Configuration
"""
from django.urls import path, include

urlpatterns = [
    # API URLS
    path('api/', include(("apps.api.urls", 'apps.api'), namespace="api")),
]