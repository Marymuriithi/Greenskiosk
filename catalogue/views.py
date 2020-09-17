from django.shortcuts import render
from  .models import Product
from .import views
# from .views import products_list

# Create your views here.


def products_list(request):
    product_image = Product.objects.all()
    return render(request, 'product_list.html', {'product_image': product_image})
    