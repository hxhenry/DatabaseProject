from django.contrib import admin

# Register your models here.
from .models import HcyAccount, HcyCustomer, HcySavings, HcyChecking, HcyLoan, HcyHome, HcyStudent, HcyState, HcyCity, HcyStreet, HcyZip,HcyUniversity

admin.site.register(HcyAccount)
admin.site.register(HcyCustomer)
admin.site.register(HcySavings)
admin.site.register(HcyChecking)
admin.site.register(HcyLoan)
admin.site.register(HcyHome)
admin.site.register(HcyStudent)
admin.site.register(HcyState)
admin.site.register(HcyCity)
admin.site.register(HcyStreet)
admin.site.register(HcyZip)
admin.site.register(HcyUniversity)