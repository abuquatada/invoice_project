from django.urls import path, include
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
   path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   path('Customers_view/',Customers_view),
   path('Products_view/',Products_view),
   path('Invoices_view/',Invoices_view),
   path('InvoicesItems_view/',InvoicesItems_view),
   path('Payments_view/',Payments_view),
   path('TaxRates_view/',TaxRates_view),
   path('CoreUser_view/',CoreUser_view),
   path('Role_view/',Role_view),
]