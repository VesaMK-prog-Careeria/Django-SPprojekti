# Tällä sivulla on URL-osoitteet, jotka ohjaavat käyttäjän
# oikeaan näkymään. Tämä on ns. reititys.
from django.urls import path
from .views import landingview, productlistview, supplierlistview, addsupplier, addproduct, \
     confirmdeleteproduct, deleteproduct, confirmdeletesupplier, deletesupplier, editproduct_get, editproduct_post

urlpatterns = [
    path('', landingview),
    # products URL
    path('products/', productlistview),
    path('add-product/', addproduct),
    path('confirm-delete-product/<int:id>/', confirmdeleteproduct),
    path('delete-product/<int:id>/', deleteproduct),
    path('edit-product-get/<int:id>/', editproduct_get),
    path('edit-product-post/<int:id>/', editproduct_post),

    # suppliers URL
    path('suppliers/', supplierlistview),
    path('add-supplier/', addsupplier),
    path('confirm-delete-supplier/<int:id>/', confirmdeletesupplier),
    path('delete-supplier/<int:id>/', deletesupplier),
]