from django.contrib import admin
from django.urls import path
from .views import product_list, product_details, upload_products
urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", product_list, name="product_list"),
    path("products/<int:product_id>/", product_details, name="details"),
    path("products/upload/", upload_products, name="upload")
    
]
    
