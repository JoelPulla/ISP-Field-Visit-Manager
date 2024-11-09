from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .forms import CustomerForm
from .models import Customer
# Create your views here.


class CustomerFormView(generic.FormView):
    template_name = "create_customer.html"
    form_class = CustomerForm
    success_url = reverse_lazy("all_customers")
    
    #save in BDD
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



class CustomerListView(generic.ListView):
    model = Customer
    template_name = "list_customer.html"
    context_object_name = 'customers'