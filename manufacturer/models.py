from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(default='', max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
