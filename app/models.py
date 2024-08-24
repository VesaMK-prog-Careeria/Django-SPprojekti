from django.db import models

class Supplier(models.Model):
    companyname = models.CharField(max_length=50, default='firma')
    contactname = models.CharField(max_length=50, default='contact')
    address = models.CharField(max_length=50, default='address')
    phone = models.CharField(max_length=50, default='phone')
    email = models.EmailField(max_length=50, default='email')
    country = models.CharField(max_length=50, default='country')

    def __str__(self):
        return f"{self.companyname} from {self.country}"

class Product(models.Model):
    productname = models.CharField(max_length=50, default='productname')
    packagesize = models.CharField(max_length=50, default='packagesize')
    unitprice = models.DecimalField(max_digits=10, decimal_places=2)
    unitsinstock = models.IntegerField(default=0)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.productname} produced by {self.supplier.companyname}"

