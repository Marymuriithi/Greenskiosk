from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class ProductSupplier(models.Model):
    GENDERS = (
        ("m", "male"),
        ("f", "female")

    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user = models.CharField(max_length=28)
    phone_number = models.IntegerField()
    street_address = models.CharField(max_length=100)
    id_number = models.IntegerField()
    date_opened = models.DateField()
    email = models.EmailField(max_length=20)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.street_address

class ProductCategory(models.Model):
    name = models.CharField(max_length=28)
    description = models.TextField(max_length=150)
    icon = models.ImageField()

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=200)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE )
    supplier_price = models.DecimalField(max_digits=6,decimal_places=2)
    selling_price = models.DecimalField(max_digits=6,decimal_places=2)
    supplier = models.ForeignKey(ProductSupplier, on_delete=models.CASCADE)
    number_in_stock = models.IntegerField()
    product=models.ImageField(upload_to='images/')
    image = models.ImageField(upload_to='galary/')
    
    def __str__(self):
        return self.title
    

