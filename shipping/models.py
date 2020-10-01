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
        return self.name


class DispenserCoolerBox(models.Model):
    box_number = models.IntegerField()
    location = models.CharField(max_length=10)
    unlock_code = models.IntegerField()

    def __str__(self):
        return self.box


class Delivery(models.Model):
    dispatch_time = models.DateTimeField()

    def __str__(self):
        return self.dispatch_time


