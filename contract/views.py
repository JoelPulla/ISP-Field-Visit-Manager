from django.shortcuts import render, get_object_or_404, redirect
from order.views import orders_by_contract
from django.contrib.auth.decorators import login_required

from .forms import ContractForm
from .models import Contract


# Create your views here.


def contracts_by_user(id_customer):
    contract = Contract.objects.filter(customer_id=id_customer)
    if not contract:
        return []
    return contract

def detail_contract(request, id_contract):
    contract = get_object_or_404(Contract, pk = id_contract)
    orders = orders_by_contract(id_contract)
    return render(request, "contract/detail.html",{
        'contract': contract,
        'orders': orders
    }) 
    

def create_contract(request, customer_id):

    if request.method == "GET":
        return render(request, "contract/create.html", {"form": ContractForm})
    form = ContractForm(request.POST)

    if form.is_valid():
        try:
            new_contract = form.save(commit=False)
            new_contract.customer_id = customer_id
            new_contract.save()
            return redirect("detail_customer", customer_id)
        except ValueError as error:
            return render(request, "contract/create.html", {"error": error})
    else:
        return render(request, "contract/create.html", {
            'form': form
        })


def update_contract(request, contract_id, ):
    contract = get_object_or_404(Contract, pk = contract_id)
    
    if request.method == "GET":
        form = ContractForm(instance=contract)
        return render(request, "contract/edit.html", {
            'form': form
        })
    
    form = ContractForm(request.POST, instance=contract)
    form.save()
    return redirect(request, "index",  )
   
  
def delete_contract(request, id_contract):
    print("HOLA MUNDO ESTE ES UN MESAJE DE PRUEBA ")
    
    if request.method == 'POST':
        contract = get_object_or_404(Contract, pk=id_contract)
        id_customer = contract.customer_id
        contract.delete()
        return redirect("detail_customer", id_customer)
    
