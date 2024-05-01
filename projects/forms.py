from django.forms import ModelForm
from .models import HcyCustomer

class HcyCustomerForm(ModelForm):
    class Meta:
        model = HcyCustomer
        fields = '__all__'