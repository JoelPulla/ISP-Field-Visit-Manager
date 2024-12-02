from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django import forms
from datetime import date
from .models import Order
from users.models import User

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['assigned_date', 'preferential_time', 'description', 'type', 'user']
        widgets = {
            'assigned_date': forms.DateInput(attrs={'type': 'date'}),
            'preferential_time': forms.TimeInput(attrs={'type': 'time'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(profile__rol="technical")
    

class UpdateOrderForm(ModelForm):
    class Meta:
        model= Order
        fields= ['assigned_date','preferential_time']
        
        widgets = {
            'assigned_date': forms.DateInput(attrs={'type': 'date'}),
            'preferential_time': forms.TimeInput(attrs={'type': 'time'}),
        }
        
    def clean_Date(self):
        order_date = self.cleaned_data["Date"]
         
        if order_date < date.today():
            raise ValidationError("No puederes reagendar para un fecha anterior a la actual")
        
        return order_date
   
         