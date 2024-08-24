# Tällä sivulla on URL-osoitteet, jotka ohjaavat käyttäjän
# oikeaan näkymään. Tämä on ns. reititys.
from django.urls import path
from .views import landingview, productlistview, supplierlistview, addsupplier, addproduct

urlpatterns = [
    path('', landingview),
    # products URL
    path('products/', productlistview),
    path('add-product/', addproduct),

    # suppliers URL
    path('suppliers/', supplierlistview),
    path('add-supplier/', addsupplier),
]