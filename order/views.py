from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.contrib import messages
from .models import Order

from contract.models import Contract
from .forms import OrderForm


# Create your views here.

def create_order(request, contract_id):
    contract = get_object_or_404(Contract, pk = contract_id)
    
    if not contract.is_active:
        messages.error(request, "El contrato esta inactivo por lo que no se puede crear Ordenes de servicio, Primero debes activar el contrato.")
        return redirect('detail_contract', contract_id)
    
    
    exist_orders = Order.objects.filter(contract_id = contract_id).exclude(status = Order.StatusChoice.COMPLETE)
    if exist_orders.exists():
        messages.error(request, "No puedes crear una nueva orden porque ya existe una orden pendiente o en progreso.")
        return redirect('detail_contract', contract_id)
        
    if request.method == "GET":
        return render (request,"order/create.html", {
                'form': OrderForm
            })
    else:
        
        form = OrderForm(request.POST)
        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.contract = contract
            new_order.save()
            messages.success(request, "Orden creada con exito")
            return redirect("all_customers")
        else:
            return render (request,"order/create.html", {
                'form': form
            })

def update_order(request,order_id):
    
    order = get_object_or_404(Order, pk = order_id)
    
    if request.method == 'GET':
        form = OrderForm(instance=order)
        return render(request, "order/update.html", {
            'form': form
        })
    else:
        form = OrderForm(request.POST, instance = order)
        if form.is_valid():
            form.save()
            return redirect("all_orders")
        else:
            return render(request, "order/update.html", {
            'form': form
        })
            
    
    
                
            
def all_ordes():
    orders = Order.objects.all()
    if not orders:
        return []
    return orders

def order_by_status(status):
    orders = Order.objects.filter(status = status)
    if not orders:
        return []
    return orders

def orders_by_contract(id_contract):
    orders = Order.objects.filter(contract_id =id_contract)

    if not orders:
        []
    return orders
    
# hacer el filtro para ordenenes pendientes, completadas y cantidad de creadas con estas tenemos 3

def orders(request):
    
    orders_pending = order_by_status(0)
    orders_complet = order_by_status(2)
    orders = all_ordes()
    
    return render(request, "order/orders.html",{
        'orders_pending': len(orders_pending),
        'orders_complet': len(orders_complet),
        'total_orders': len(orders),
        'orders': orders
    })

def delete_order(request, order_id):
    if request.method == 'POST':
        order = get_object_or_404(Order, pk= order_id)
        order.delete()
        redirect("all_orders")
        

        
