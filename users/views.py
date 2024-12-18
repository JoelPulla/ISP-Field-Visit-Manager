from django.shortcuts import redirect, render
from .models import Profile
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def redirect_custom_login(request):
    if not request.user.is_authenticated:
        return redirect("login")
    try:
        profile = Profile.objects.get(user=request.user)
        if profile.rol == "admin":
            return  redirect("index")
        elif profile.rol == "technical":
            return redirect("order_by_user")         
    except profile.DoesNotExist: 
                print("NO EXISTE")
   
    return redirect("no page")
              
        
    
