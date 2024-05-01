from django.shortcuts import render, redirect
from .models import HcyCustomer
from .forms import HcyCustomerForm


# Create your views here.
def customer_review(request):
    return None


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def customer_add(request):
    form = HcyCustomerForm()
    if request.method == 'POST':
        form = HcyCustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("customer_review")

    context = {'form': form}
    return render(request, 'customer_add.html', context)
