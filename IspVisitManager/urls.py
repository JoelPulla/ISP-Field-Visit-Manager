"""
Global Urls
"""
from django.contrib import admin
from django.urls import path, include

from dash.views import HomeView


urlpatterns = [
    path("", HomeView, name="index"),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls') ),
    path("customer/", include("customer.urls")),
    path("contract/", include("contract.urls")),
    path("orders/", include('order.urls'),)
    
]
