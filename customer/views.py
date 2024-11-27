from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy

from .forms import CustomerForm
from .models import Customer
from contract.views import contracts_by_user
# Create your views here.



def detail_customer(request, id_customer):
    customer = get_object_or_404(Customer, id= id_customer)
    contracts = contracts_by_user(id_customer= id_customer)
    
    return render(request, "customer/detail.html",{
        "customer": customer,
        "id" : id_customer,
        "contracts": contracts
    })

def create_customer(request ):
    
    if request.method == 'GET':
        return render(request, 'customer/create.html',{
            'form' : CustomerForm
        })
    else:
        form = CustomerForm(request.POST)
        if form.is_valid():
            try:
                new_customer = form.save(commit=False)
                new_customer.save()
                return redirect("all_customers")

            except Exception as error:
                return render(request, 'customer/create.html',{
                    'form': form,
                    'error': f"Error al guardar el cliente por: {error}"
                })
        else:
            return render(request,"customer/create.html", {
                'form': form
            })
    
    
    
    
    
    
    
def update_customer(request, id_customer):
    customer = get_object_or_404(Customer, pk =id_customer)
    
    if request.method == "GET":
        form = CustomerForm(instance=customer)
        return render(request, "customer/edit.html", {
            'form' : form
        })
    else:
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect("detail_customer", id_customer)
        else:
            return render(request, "customer/edit.html", {'form': form})

            
def delete_customer(request, id_customer):
    if request.method == 'POST':
        customer = get_object_or_404(Customer, pk=id_customer)
        if customer:
            customer.delete()
            return redirect("all_customers")
        else:
            return render(request, "customer/list_customer.html", {
                'error' : "error al eliminar el cliente en el servidor "
        })    
    
class CustomerListView(generic.ListView):
    model = Customer
    template_name = "customer/list_customer.html"
    context_object_name = 'customers'