from django.contrib import admin
from django.urls import path
from .views import product_list, product_details, upload_products, add_to_cart
urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", product_list, name="product_list"),
    path("products/<int:product_id>/", product_details, name="details"),
    path("products/upload/", upload_products, name="upload")
    #path("cart/<int:product_id>/", add_to_cart, name="add"),
    #path("cart/", views.get_cart, name="cart"),
    
]
    
