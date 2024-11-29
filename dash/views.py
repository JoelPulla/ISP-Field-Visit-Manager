from django.shortcuts import render
from customer.views import all_customers
from order.views import order_by_status
# Create your views here.

def HomeView(request):
    
    customers = all_customers()
    orders_pending = len(order_by_status(0))
    orders_complete = len(order_by_status(2))

    return render(request, 'index.html',{
        'total_customer' : len(customers),
        'orders_pending': orders_pending,
        'orders_complete': orders_complete,
        'customers': customers
    })