from django.db import models


class VehicleLine(models.Model):
    name = models.CharField(default='', max_length=100)
    description = models.TextField(default='')

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(default='', max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class HirePoint(models.Model):
    name = models.CharField(default='', max_length=100)
    phone = models.CharField(default='', max_length=20)
    address_line1 = models.CharField(default='', max_length=100)
    address_line2 = models.CharField(default='', max_length=100)
    address_line3 = models.CharField(default='', max_length=100)
    description = models.TextField(default='')

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    name = models.CharField(default='', max_length=500)
    vehicle_line = models.ForeignKey(VehicleLine, default='', on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, default='', on_delete=models.CASCADE)
    hire_point = models.ForeignKey(HirePoint, default='', on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    rent_price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='Pictures')
    rating = models.PositiveSmallIntegerField(default=0)
    description = models.TextField()

    def __str__(self):
        return self.name
