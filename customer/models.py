from django.db import models

# Create your models here.
class Customer(models.Model):
    ci= models.CharField(max_length=13,null=False, verbose_name="Cedula o Ruc" )
    name= models.CharField(max_length=50, null=False, verbose_name="nombre")
    last_name= models.CharField(max_length=50, null=False, verbose_name="Apellido")
    address = models.CharField(max_length=50, null=False, verbose_name="Dirección")
    number = models.CharField( max_length=10, null= False, verbose_name="Número")
    mail = models.EmailField(null=True, verbose_name="Correo electronico" )
    create_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.name
    