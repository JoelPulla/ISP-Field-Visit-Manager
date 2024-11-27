from django.db import models

from customer.models import Customer
# Create your models here.

class Plan(models.Model):
    name = models.CharField(max_length=20, null=False, verbose_name="Nombre")
    megabytes = models.CharField(max_length=4, null= False, verbose_name="Megabytes")
    price= models.FloatField( verbose_name="Precio")
    
    def __str__(self):
        return f"{self.name} / {self.megabytes} MB "
    
    
class Contract(models.Model):
    address = models.CharField(max_length=50, verbose_name="Dirección", null=False)
    coordinates = models.CharField(max_length=200, verbose_name="Coordenadas Ubicación", null=True, blank=True)
    url_gps = models.URLField(verbose_name="URL GPS", null=True, blank=True)
    box = models.CharField(max_length=200, verbose_name="Coordenadas Caja", null=True, blank=True)
    ont = models.CharField(max_length=200, verbose_name="SN ONT", null=True, blank=True)
    router = models.CharField(max_length=200, verbose_name="SN Router", null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name="Status Activo")
    created_at = models.DateTimeField(auto_now_add=True)

    plan = models.ForeignKey(Plan, on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return f"Contrato #{self.id} - {self.customer}"

    