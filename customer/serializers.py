from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'ci', 'is_active', 'name','last_name', 'address', 'number', 'mail' )
        read_only_fields = ['create_at']