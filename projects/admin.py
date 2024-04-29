from django.contrib import admin

# Register your models here.
from .models import Account, Customer

admin.site.register(Account)
admin.site.register(Customer)
