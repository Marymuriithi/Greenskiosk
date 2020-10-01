from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products':products})

def product_details(request, product_id):
    product = Product.objects.filter(id=product_id)
    # images = product.images.all()
    return render(request, 'product_details.html', {'product':product})

def upload_products(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('products_list')
    else:
        form = ProductForm
    return render(request, 'upload_products.html', {'form': form} )





