from django.db import models
from user.models import CustomerUser
from cart.models import cart

# Create your models here.


class orders(models.Model):
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    cart = models.ForeignKey(cart, on_delete=models.CASCADE)
    #shipping_address = models.CharField(default='', max_length=255)
    is_shipping = models.BooleanField(default=False)
    description = models.TextField(default='')
    totalPrice = models.IntegerField(default=0)
    is_rented = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)


class shipping(models.Model):
    order = models.ForeignKey(orders, on_delete=models.CASCADE)
    address = models.CharField(default='', max_length=255)
    orderDate = models.DateTimeField(auto_now_add=True)
    requiredDate = models.DateTimeField(null=True, blank=True)
    shippedDate = models.DateTimeField(null=True, blank=True)
    status = models.CharField(default='', max_length=255)
    description = models.TextField(default='')


class orderHistory(models.Model):
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    order = models.ForeignKey(orders, on_delete=models.CASCADE)

