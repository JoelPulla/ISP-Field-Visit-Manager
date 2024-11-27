from django.db import models
from django.utils.translation import gettext_lazy

from users.models import User
from contract.models import Contract

# Create your models here.

class Type(models.Model):
    name = models.CharField(null=False, blank=False, verbose_name="Nombre", max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Order(models.Model): 
    #choices the status     
    class StatusChoice(models.IntegerChoices):
        PENDING = 0,gettext_lazy("Pendiente")
        IN_PROCESS = 1, gettext_lazy("En progreso")
        COMPLETE = 2, gettext_lazy("Completo")
    
    status = models.IntegerField(default=StatusChoice.PENDING, choices=StatusChoice.choices)
    assigned_date= models.DateField(verbose_name="Fecha preferencial")
    preferential_time = models.TimeField( auto_now=False, auto_now_add=False, verbose_name="Hora preferencial", null=False)
    description = models.TextField(max_length=300, verbose_name="Description del problema", null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    #relations
    type = models.ForeignKey(Type,on_delete=models.PROTECT, null=False)
    contract = models.ForeignKey(Contract, on_delete=models.PROTECT, related_name="Responsable")
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    order_attetions = models.OneToOneField("Order_attentions", verbose_name=("Orden de solucion "), on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return super().__str__()


class Order_attentions(models.Model):
    entry_time = models.TimeField( auto_now=False, auto_now_add=False, verbose_name="Hora de entrada", null=False)
    final_time = models.TimeField( auto_now=False, auto_now_add=False, verbose_name="Hora de salida", null=False)
    diagnostic = models.TextField(max_length=300, verbose_name="Diagnostico diagnostico", null=False, blank=False, )
    pot_final = models.DecimalField(decimal_places=2, max_digits=4, null=False, verbose_name="Potencia final")
    action_corrective = models.TextField(null=False, max_length=100, verbose_name="Diagnostico del problema")
    remote_managment = models.BooleanField(null=False, default=False, verbose_name="Accesso remoto")
    aditional_note = models.TextField(max_length=1000, null=True, verbose_name="Nota adicional")
    soluttion_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return super().__str__()
