from django.urls import path
from .views import *

urlpatterns = [
    path("<int:contract_id>/orders/create", create_order, name="create_order")
]
 