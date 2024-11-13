from django.db import models

from customer.models import Customer
# Create your models here.

class Plan(models.Model):
    name = models.CharField(max_length=20, null=False, verbose_name="Nombre")
    mgbytes = models.CharField(max_length=4, null= False, verbose_name="Megabytes")
    price= models.FloatField( verbose_name="Precio")
    
    def __str__(self):
        return self.name
    
    
class Contract(models.Model):
    address = models.CharField(max_length=50, verbose_name="Direccion", null=False)
    coordinates = models.CharField(max_length=200,verbose_name="Cordenadas Ubicacion")
    url_gps = models.URLField(verbose_name="Url Gps ")
    box = models.CharField(max_length=200,verbose_name="Coordenadas Caja")
    ont = models.CharField(max_length=200,verbose_name="Sn Ont", null=False)
    router = models.CharField(max_length=200,verbose_name="Sn Router")
    is_active = models.BooleanField(default=True, verbose_name="Status Activo ")
    created_at= models.DateTimeField(auto_now_add=True)
    
    
    plan = models.OneToOneField(Plan, on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False, blank=False)
    
    def __str__(self):
        return self.id
    