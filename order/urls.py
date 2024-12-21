from django.urls import path
from .views import *


urlpatterns = [
    path("", orders, name="all_orders"),
    path("<int:order_id>/update", update_order, name="update_order"),
    path("<int:contract_id>/create", create_order, name="create_order"),
    path("<int:order_id>/delete", delete_order, name="delete_order"),
    ##tecnical
    path("tecnico/", order_by_user, name="order_by_user"),
    path("tecnico/<int:order_id>/complete", complete_order, name="complete_order"),
    path(
        "tecnico/<int:order_id>/cancel_order/",
        cancel_order,
        name="cancel_order_by_user",
    ),
    path(
        "tecnico/<int:order_id>/reagender/", reschecule_order, name="reschecule_order"
    ),
    path("apiv1/ordersByUser", OrderListView.as_view()),
]
