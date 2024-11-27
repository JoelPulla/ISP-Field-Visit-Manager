from django.forms import ModelForm, forms

from .models import Customer
#your forms 

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['ci', 'name', 'last_name', 'address', 'number', 'mail']

    

    def clean_ci(self):
        ci = self.cleaned_data.get("ci")

        # Validar longitud de `ci`
        if not ci or len(ci) not in [10, 13]:
            raise forms.ValidationError(
                "El número de identificación debe tener 10 o 13 dígitos correspondientes a la cédula o RUC."
            )
        
        # Validar si ya existe otro cliente con el mismo `ci`
        instance = self.instance
        if Customer.objects.filter(ci=ci).exclude(pk=instance.pk).exists():
            raise forms.ValidationError(
                "Ya existe un cliente con ese número de identificación."
            )
        return ci
