from django.forms import ModelForm, forms

from .models import Customer
#your forms 

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['ci', 'name', 'last_name', 'address', 'number', 'mail']

    def clean_ci(self):
        ci = self.cleaned_data.get("ci")
        if len(ci) not in [10,13]:
            raise forms.ValidationError("El numero de indentificacion debe tener 10 0 13 digitios correspondientes a la cedula o ruc")
        return ci
    