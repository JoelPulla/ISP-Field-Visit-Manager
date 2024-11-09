from django.urls import path

from .views import CustomerFormView, CustomerListView

urlpatterns = [
    path("create/",CustomerFormView.as_view(), name="create_customer"),
    path("all/",CustomerListView.as_view(), name="all_customers" )
]
