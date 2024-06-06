from django.contrib import admin

# Register your models here.
from .models import Customers
from .models import Products
from .models import Invoices
from .models import InvoiceItems
from .models import TaxRates
from .models import CoreUser
from .models import Role



admin.site.register(Customers)
admin.site.register(Products)
admin.site.register(Invoices)
admin.site.register(InvoiceItems)
admin.site.register(TaxRates)
admin.site.register(CoreUser)
admin.site.register(Role)



