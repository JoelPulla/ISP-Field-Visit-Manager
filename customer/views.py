from django.shortcuts import render, get_list_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy

from .forms import CustomerForm
from .models import Customer
# Create your views here.

#mejorar logica de creacion evitar usaurios con el mismo numero y con mismo bombre 



def create_customer(request ):
    if request.method == 'GET':
        return render(request, 'customer/create.html',{
            'form' : CustomerForm
        } )
    else: 
        ci = "0106817612"
        form = CustomerForm(request.POST)
        new_customer = form.save(commit=False)
        filter_user = Customer.objects.filter(ci=ci)
        try:
            if not filter_user:
                new_customer.name = new_customer.name.lower()
                new_customer.save()
                return reverse_lazy("all_customers")
            else:
                return render(request, 'customer/create.html',{
                    'error': "error al crear un cliente por que ya existe con ese numero de identificacion",
                    'form':CustomerForm
                })
        except Exception as error:
            return render(request, 'customer/create.html',{
                    'error': f"error en el servidor por: {error}"
                })
    
def update_customer(request, id_customer):
    customer = get_list_or_404(Customer, pk =id_customer)
    if request.method == "GET":
        form = CustomerForm(instance=customer)
        return render(request, "customer/edit.html", {
            'form' : 'form'
        })
    else:
        form = CustomerForm(request.POST, instance=customer)
        form.save()
        return redirect("index")
        
    
    
    
def delete_customer(request, id_customer):
    if request.method == 'POST':
        customer = get_list_or_404(Customer, pk=id_customer)
        if customer:
            customer.delete()
        else:
            return render(request, "customer/list_customer.html", {
                'error' : "error al eliminar el cliente en el servidor "
        })    
    
    


class CustomerListView(generic.ListView):
    model = Customer
    template_name = "customer/list_customer.html"
    context_object_name = 'customers'