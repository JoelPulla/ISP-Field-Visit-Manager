from django.forms import ModelForm
from .models import Contract

class ContractForm(ModelForm):
    
    class Meta:
        model = Contract
        fields = ['address', 'url_gps', 'plan',]
