from django.shortcuts import render
from  .models import Product
from .import views
# from .views import product_list

# Create your views here.


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def upload_product(request):
    form = ProductForm()
    return render(request, 'upload_product.html', {'form': form})
    
                                                                                     