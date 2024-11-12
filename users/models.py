from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.CharField(max_length=50, choices=[
        ('admin','Administrador'),
        ('technical','Tecnico')
    ])
    
    def __str__(self):
        return self.rol