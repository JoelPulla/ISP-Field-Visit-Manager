from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django import forms
from datetime import date
from .models import Order, Order_attentions
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
        
    def clean_assigned_date(self):
        order_date = self.cleaned_data["assigned_date"]
         
        if order_date < date.today():
            raise ValidationError("No puederes reagendar para un fecha anterior a la actual")
        
        return order_date
   
class CompleteOrderForm(ModelForm):
    class Meta:
        model = Order_attentions
        fields = ['entry_time', 'final_time', 'diagnostic', 'pot_final', 'action_corrective', 'remote_managment', 'aditional_note']
        
        widgets = {
            'entry_time':forms.TimeInput(attrs={'type':'time'}),
            'final_time':forms.TimeInput(attrs={'type':'time'})
        }