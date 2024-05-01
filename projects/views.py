from django.shortcuts import render
from .models import HcyCustomer


# Create your views here.
def customer_view(request):
    customer = HcyCustomer.objects.first()  # Assuming there's only one customer for simplicity
    return render(request, 'customer.html', {'customer': customer})


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')
