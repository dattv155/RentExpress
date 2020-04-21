from django.db import models
from product.models import variations
from user.models import CustomerUser

# Create your models here.

class cart(models.Model):
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class cartItem(models.Model):
    cart = models.ForeignKey(cart, on_delete=models.CASCADE)
    item = models.ForeignKey(variations, on_delete=models.CASCADE)
    quantityOrdered = models.IntegerField(default=0)
    priceEach = models.IntegerField(default=0)
