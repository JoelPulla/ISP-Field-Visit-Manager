from django.urls import path

from .views import *

urlpatterns = [
    
    # path("", AllContractViews.as_view(), name="list_contracts"), 
    path("customer/<int:customer_id>/create/", create_contract, name="create_contract"),
    path("customer/<int:customer_id>/edit", update_contract, name="update_contract")
]
