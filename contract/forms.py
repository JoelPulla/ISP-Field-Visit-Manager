from django.forms import ModelForm

from .models import Contract

class ContractForm(ModelForm):
    
    class Meta:
        model = Contract
        fields = ['address','coordinates', 'url_gps', 'box', 'ont', 'router','plan', 'customer' ]
