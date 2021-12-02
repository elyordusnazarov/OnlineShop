import datetime
import django
from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=125, null=True, blank=True)
    image = models.ImageField(null=True, blank=True,upload_to="catimage")
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Products(models.Model):
    category = models.ForeignKey(to=Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=125, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='primage')
    discount = models.IntegerField(null=True, blank=True, default=0)
    price = models.IntegerField(null=True, blank=True)
   

    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            return ''

    def __str__(self):
        return self.name


class Savatcha(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Products, models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True,default=1)
    sold_price = models.IntegerField(null=True, default=0)

    class Payment(models.TextChoices):
        cash = '1', "Naqd"
        card = '2', "Card"
        etulov = '3', "Eto'lov"

    payment_type = models.CharField(
        max_length=55,
        choices=Payment.choices,
        default=Payment.cash
    )
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=25, null=True)

    def __str__(self):
        return f"{self.product.name}    {self.quantity}"



class Wishlist(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    product=models.ForeignKey(Products,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return f"{self.username} {self.name}"





