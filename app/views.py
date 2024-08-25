# Tällä sivulla on näkymät, jotka näytetään käyttäjälle.
# sekä mallien tuonti, joilla voidaan hakea tietoa tietokannasta.
from django.shortcuts import render, redirect
from .models import Supplier, Product # . tarkoittaa nykyistä hakemistoa

def landingview(request):
    return render(request, 'landingpage.html')

# --------------------------------------------------Product view
# Product modelin tuonti
def productlistview(request):
    productlist = Product.objects.all()
    supplierlist = Supplier.objects.all()
    context = {'products': productlist, 'suppliers': supplierlist}
    return render (request,"productlist.html",context)

#region Add, delete, edit product
def addproduct(request):
    a = request.POST['productname']
    b = request.POST['packagesize']
    c = request.POST['unitprice']
    d = request.POST['unitsinstock']
    e = request.POST['supplier']
    
    Product(productname = a, packagesize = b, unitprice = c, unitsinstock = d, supplier = Supplier.objects.get(id = e)).save()
    return redirect(request.META['HTTP_REFERER'])

def searchproduct(request):
    search = request.POST['search']
    productlist = Product.objects.filter(productname__contains = search) #icontains = case insensitive, contains = case sensitive
    context = {'products': productlist}
    return render(request, 'productlist.html', context)

def confirmdeleteproduct(request, id):
    product = Product.objects.get(id = id)
    context = {'product': product}
    return render(request, 'confirmdelprod.html', context)

def deleteproduct(request, id):
    Product.objects.get(id = id).delete()
    return redirect(productlistview)

def editproduct_get(request, id):
    product = Product.objects.get(id = id)
    supplierlist = Supplier.objects.all()
    context = {'product': product, 'suppliers': supplierlist}
    return render(request, 'edit_prod.html', context)

def editproduct_post(request, id):
    product = Product.objects.get(id = id)
    product.productname = request.POST['productname']
    product.packagesize = request.POST['packagesize']
    product.unitprice = request.POST['unitprice']
    product.unitsinstock = request.POST['unitsinstock']
    product.supplier = Supplier.objects.get(id = request.POST['supplier'])
    product.save()
    return redirect(productlistview)

def suppliers_products(request, id):
    supplier = Supplier.objects.get(id = id)
    products = Product.objects.filter(supplier = supplier)
    context = {'supplier': supplier, 'products': products}
    return render(request, 'productlist.html', context)
#endregion

# --------------------------------------------------Supplier view
# Supplier modelin tuonti
def supplierlistview(request):
    supplierlist = Supplier.objects.all()
    context = {'suppliers': supplierlist}
    return render (request,"supplierlist.html",context)

#region Add, delete, edit supplier
def addsupplier(request):
    a = request.POST['companyname']
    b = request.POST['contactname']
    c = request.POST['address']
    d = request.POST['phone']
    e = request.POST['email']
    f = request.POST['country']
    Supplier(companyname = a, contactname = b, address = c, phone = d, email = e, country = f).save()
    return redirect(request.META['HTTP_REFERER'])

#region Vaihtoehtoinen tapa lisätä Supplier
# from django.forms import ModelForm
# from .models import Supplier
# class SupplierForm(ModelForm):
#     class Meta:
#         model = Supplier
#         fields = '__all__' #or put the fields you want in list


# def addsupplier(request):
#     form = SupplierForm(request.POST or None)
#     if(form.is_valid()):
#         form.save() 
#         return redirect(request.META['HTTP_REFERER'])
#     else:
#         return render(request, 'template', context)
#endregion

def searchsupplier(request):
    search = request.POST['search']
    supplierlist = Supplier.objects.filter(companyname__contains = search) #icontains = case insensitive, contains = case sensitive
    context = {'suppliers': supplierlist}
    return render(request, 'supplierlist.html', context)

def confirmdeletesupplier(request, id):
    supplier = Supplier.objects.get(id = id)
    context = {'supplier': supplier}
    return render(request, 'confirmdelsupp.html', context)

def deletesupplier(request, id):
    Supplier.objects.get(id = id).delete()
    return redirect(supplierlistview)

def editsupplier_get(request, id):
    supplier = Supplier.objects.get(id = id)
    context = {'supplier': supplier}
    return render(request, 'edit_supp.html', context)

def editsupplier_post(request, id):
    supplier = Supplier.objects.get(id = id)
    supplier.companyname = request.POST['companyname']
    supplier.contactname = request.POST['contactname']
    supplier.address = request.POST['address']
    supplier.phone = request.POST['phone']
    supplier.email = request.POST['email']
    supplier.country = request.POST['country']
    supplier.save()
    return redirect(supplierlistview)
#endregion
