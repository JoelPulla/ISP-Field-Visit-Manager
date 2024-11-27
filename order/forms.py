from typing import Any
from django.forms import ModelForm

from .models import Order
from users.models import User

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['assigned_date', 'preferential_time', 'description', 'type', 'user']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['user'].queryset = User.objects.filter(profile__rol="technical")