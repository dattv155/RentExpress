from django.db import models


class Vehicle(models.Model):
    name = models.CharField(default='', max_length=500)
    manufacturer = models.CharField(default='', max_length=100)
    quantity = models.PositiveSmallIntegerField(default=0)
    rent_price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='Pictures')
    rating = models.PositiveSmallIntegerField(default=0)
    description = models.TextField()

    def __str__(self):
        return self.name

