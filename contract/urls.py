from django.urls import path

from .views import ContractForm, AllContractViews


urlpatterns = [
    path("", AllContractViews.as_view(), name="list_contracts"), 
    path("create/", ContractForm.as_view(), name="create_contract"),
]
