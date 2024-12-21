from rest_framework import serializers
from .models import Order


class OrderSerializazer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "status",
            "assigned_date",
            "preferential_time",
            "description",
            "created_at",
            "type",
            "contract",
            "user",
            "order_attetions",
        ]
