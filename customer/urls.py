from django.urls import path

from .views import *

urlpatterns = [
    
    path("",CustomerListView.as_view(), name="all_customers" ),
    path("create/", create_customer, name="create_customer"),
    path("<int:id_customer>/",detail_customer, name="detail_customer"),
    path("<int:id_customer>/delete/", delete_customer, name="delete_customer"),
    path("<int:id_customer>/edit/", update_customer, name="update_customer")
]
