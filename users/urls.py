
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import redirect_custom_login

urlpatterns = [
    
    path("login/", LoginView.as_view(template_name = "login.html"), name="login"),
    path("redirect/",redirect_custom_login , name="redirect"),
    path("logout/", LogoutView.as_view(), name="logout")
    
    
]