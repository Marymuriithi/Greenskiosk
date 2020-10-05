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
    return render(request, 'upload_product.html', {'form': form} )

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    product = Product.objects.get(id=product_id)
    cart[product_id] = product
    request.session['cart'] = cart
    return HttpResponseRedirect(reverse("cart"))


# Cart View
def get_cart(request):
    cart = request.session.get('cart',{})
    return render(request, 'buylist/add_to_cart.html', cart)





