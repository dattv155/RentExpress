from django.db import models
from profiles.models import User
from vehicles.models import Vehicle


class Discount(models.Model):
    promo_code = models.CharField(default='', max_length=15)
    discount = models.IntegerField(default=0)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    description = models.TextField(default='')

    def __str__(self):
        return self.promo_code


class Rental(models.Model):
    customer = models.ForeignKey(User, default='', on_delete=models.CASCADE)
    rental_start_time = models.DateTimeField(null=True, blank=True)
    rental_end_time = models.DateTimeField(null=True, blank=True)
    discount = models.ForeignKey(Discount, default='', on_delete=models.CASCADE)
    description = models.TextField()


class RentalDetail(models.Model):
    rental = models.ForeignKey(Rental, default='', on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, default='', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    price_each = models.IntegerField(default=0)
