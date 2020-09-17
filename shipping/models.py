from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ShippingProvider(models.Model):

    name = models.CharField(max_length= 10)
    date_joined = models.DateField()
    email = models.EmailField()
    phone_number = models.IntegerField()
    transport_mode = models.CharField(max_length=10)

    def __str__(self):
        return self.Shipping_Provider()


class DispenserCoolerBox(models.Model):
    box_number = models.IntegerField()
    location = models.CharField(max_length=10)
    unlock_code = models.IntegerField()

    def __str__(self):
        return self.box()


class Delivery(models.Model):
    # order = models.ForeignKey(Order, on_delete=models.CASCADE)
    dispatch_time = models.DateTimeField()
    # shipping = models.ForeignKey(ShippingProvider)
    # cooler_box = models.ForeignKey()

    def __str__(self):
        return self.delivery()


