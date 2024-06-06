from django.urls import path, include
from .views import *



urlpatterns = [
   path('Customers/',CustomersView.as_view()),
   path('Products_view/',Products_view),
   path('Invoices_view/',Invoices_view),
   path('InvoicesItems_view/',InvoicesItems_view),
   path('Payments_view/',Payments_view),
   path('TaxRates_view/',TaxRates_view),
   path('CoreUser_view/',CoreUser_view),
   path('Role_view/',Role_view),
   # path('customer_rawquery/',customer_query)
]