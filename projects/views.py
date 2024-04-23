from django.shortcuts import render


# Create your views here.
def customer(request):
    return render(request, 'customer.html')


def employee(request):
    return render(request, 'employee.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')
