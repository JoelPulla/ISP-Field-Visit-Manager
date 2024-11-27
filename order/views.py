from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Order

from contract.models import Contract
from .forms import OrderForm


# Create your views here.

def create_order(request, contract_id):
    
    contract = get_object_or_404(Contract, pk = contract_id)
    if not contract.is_active:
        messages.error(request, "El contrato esta inactivo por lo que no se puede crear Ordenes de servicio, Primero debes activar el contrato.")
        return redirect('all_customers')
    
    
    exist_orders = Order.objects.filter(contract_id = contract_id).exclude(status = Order.StatusChoice.COMPLETE)
    if exist_orders.exists():
        messages.error(request, "No puedes crear una nueva orden porque ya existe una orden pendiente o en progreso.")
        return render("all_customers")
        
    if request.method == "GET":
        return render (request,"order/create.html", {
                'form': OrderForm
            })
    else:
        form = OrderForm(request.POST)
        new_order = form.save(commit=False)
        new_order.contract = contract
        new_order.save()
        messages.success(request, "Orden creada con exito")
        return redirect("all_customers")
     