from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy

from .forms import ContractForm
from .models import Contract
# Create your views here.


def contracts_by_user(id_customer):
    contract = Contract.objects.filter(customer_id = id_customer)
    if not contract:
        return []
    return contract

class ContractForm(generic.FormView):
    template_name = "add_contract.html" 
    form_class = ContractForm
    reverse_lazy = "all_contracts"
    
class AllContractViews(generic.ListView):
    model = Contract
    template_name = "list_contracts.html"
    context_object_name = 'contracts'
    
    