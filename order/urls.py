from django.urls import path
from .views import *

urlpatterns = [
    path("", orders, name="all_orders"),
    path("<int:order_id>/update",update_order, name="update_order"),
    path("<int:contract_id>/create", create_order, name="create_order")
]
 