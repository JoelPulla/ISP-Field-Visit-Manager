from django.forms import ModelForm

from .models import Customer
#your forms 

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['ci', 'name', 'last_name', 'address', 'number', 'mail']
