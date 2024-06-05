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


@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):
    list_display = Customers.DisplayField

    search_fields = Customers.SearchField

    list_filter = Customers.FilterField


# admin.site.register(Products)
@admin.register(Products)
class CustomersAdmin(admin.ModelAdmin):
    list_display = Products.DisplayField

    search_fields = Products.SearchField
    list_filter = Products.FilterField



# admin.site.register(Invoices)
@admin.register(Invoices)
class InvoicesAdmin(admin.ModelAdmin):
    list_display = Invoices.DisplayField

    search_fields = Invoices.SearchField
    list_filter = Invoices.FilterField


    
# admin.site.register(InvoiceItems)
@admin.register(InvoiceItems)
class InvoiceItemsAdmin(admin.ModelAdmin):
    list_display = InvoiceItems.DisplayField

    search_fields = InvoiceItems.SearchField
    list_filter = InvoiceItems.FilterField



# admin.site.register(TaxRates)
@admin.register(TaxRates)
class TaxRatesAdmin(admin.ModelAdmin):
    list_display = TaxRates.DisplayField

    search_fields = TaxRates.SearchField
    list_filter = TaxRates.FilterField



# admin.site.register(CoreUser)
@admin.register(CoreUser)
class CoreUserAdmin(admin.ModelAdmin):
    list_display = CoreUser.DisplayField

    search_fields = CoreUser.SearchField
    # list_filter = CoreUser.FilterField



# admin.site.register(Role)
@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = Role.DisplayField

    search_fields = Role.SearchField
    list_filter = Role.FilterField

