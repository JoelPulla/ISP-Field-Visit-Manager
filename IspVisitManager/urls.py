"""
Global Urls
"""
from django.contrib import admin
from django.urls import path, include

from dash.views import HomeView


urlpatterns = [
    path("", HomeView),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls') ),
    path("customers/", include("customer.urls")),
    path("contract/", include("contract.urls"))
    
]
