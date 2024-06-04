from django.contrib import admin

from .models import Customers
from .models import Products
from .models import Invoices
from .models import InvoiceItems
from .models import TaxRates
from .models import CoreUser
from .models import Role

# from .models import UserManager


# Register your models here.

admin.site.register(Customers)
admin.site.register(Products)
admin.site.register(Invoices)
admin.site.register(InvoiceItems)
admin.site.register(TaxRates)
admin.site.register(CoreUser)
admin.site.register(Role)

# admin.site.register(UserManager)