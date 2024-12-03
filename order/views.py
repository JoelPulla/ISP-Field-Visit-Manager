from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.contrib import messages
from .models import Order
from django.db.models import Q

from contract.models import Contract
from customer.models import Customer
from .forms import OrderForm, UpdateOrderForm, CompleteOrderForm


# Create your views here.

def create_order(request, contract_id):
    contract = get_object_or_404(Contract, pk = contract_id)
    
    if not contract.is_active:
        messages.error(request, "El contrato esta inactivo por lo que no se puede crear Ordenes de servicio, Primero debes activar el contrato.")
        return redirect('detail_contract', contract_id)

    exist_orders = Order.objects.filter(contract_id=contract_id).exclude(
        Q(status=Order.StatusChoice.COMPLETE) | Q(status=Order.StatusChoice.CANCELED)  
    )

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
            return redirect('detail_contract', contract_id)
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
        contract_id = order.contract_id
        order.delete()
        return redirect("detail_contract", contract_id)
        
#### orders by technical 
def order_by_user(request):
    # Usamos select_related para optimizar las consultas y evitar consultas N+1
    orders = Order.objects.select_related('contract__customer').filter(user=request.user, status = 0)

    # Crear una lista con los datos que vamos a pasar a la plantilla
    ords = [{
        'order_id': order.id,
        'type': order.type,
        'assigned_date': order.assigned_date,
        'preferential_time': order.preferential_time,
        'address': order.contract.address,
        'name': order.contract.customer.name,
        'lat_name': order.contract.customer.last_name,
    } for order in orders]

    # Pasar los datos al template
    return render(request, "tecnical/home_orders.html", {'ords': ords})
        
def reschecule_order(request, order_id):
    
    order = get_object_or_404(Order, pk=order_id)
    
    
    if request.method == "GET":
        form = UpdateOrderForm(instance=order)
        return render(request, "order/reagender.html",{
            'form': form
        })
    else:
        form = UpdateOrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return  redirect("order_by_user")
        else:
            return render(request, "order/reagender.html",{
                'form': form
            })
        
def complete_order(request, order_id):
    
    if request.method == "GET":
        form = CompleteOrderForm
        return render(request, "order/complete.html", {'form':form})
    
    else:
        form = CompleteOrderForm(request.POST)
        save_form = form.save()
        
        #vincula con la orden principal
        order = get_object_or_404(Order, pk=order_id)
        order.order_attetions = save_form
        order.status = 2
        order.save()
        messages.success(request,f"Ordern {order_id} Data de baja")
        return redirect("order_by_user")  
             
def cancel_order(request, order_id):
    order = get_object_or_404(Order, id = order_id)
    if request.method == "POST":
        order.status = 3
        order.save()
        messages.success(request,f"Ordern {order_id} marcada como cancelada")
        return redirect("order_by_user")    
        
        
        