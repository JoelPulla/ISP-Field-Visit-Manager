from django.urls import path

from .views import *

urlpatterns = [
    
    # path("", AllContractViews.as_view(), name="list_contracts"), 
    path("<int:id_contract>", detail_contract, name="detail_contract"),
    path("customer/<int:customer_id>/create/", create_contract, name="create_contract"),
    path("customer/<int:customer_id>/edit/", update_contract, name="update_contract"),
    path("<int:id_contract>/delete/", delete_contract, name="delete_contract"),
    
]
