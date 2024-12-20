from django.urls import path
from .views import *
from rest_framework import routers
from .api import CustomerViewSet
from django.urls import path, include

#Django 
urlpatterns = [
    path("",CustomerListView.as_view(), name="all_customers" ),
    path("create/", create_customer, name="create_customer"),
    path("<int:id_customer>/",detail_customer, name="detail_customer"),
    path("<int:id_customer>/delete/", delete_customer, name="delete_customer"),
    path("<int:id_customer>/edit/", update_customer, name="update_customer")
]

# Rest Framework 
router = routers.DefaultRouter()
router.register('api/customers', CustomerViewSet, 'customers')
urlpatterns += [
    path('', include(router.urls)),
]