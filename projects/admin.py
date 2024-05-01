from django.contrib import admin

# Register your models here.
from .models import HcyAccount, HcyCustomer

admin.site.register(HcyAccount)
admin.site.register(HcyCustomer)
