from django.urls import path
from .import views
from .views import product_list
from .views import upload_product

urlpatterns = [
    path('products/', product_list, name='product-list'),
    path("products/upload/", upload_product, name="product-uploads")
]