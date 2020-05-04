from django.db import models

# Create your models here.


class productlines(models.Model):
    productLineName = models.CharField(default='', max_length=100)
    slug =  models.CharField(default='', max_length=100)
    description = models.TextField(default='')

    def __str__(self):
        return self.productLineName


class products(models.Model):
    productName = models.CharField(default='', max_length=100)
    productLine = models.ForeignKey(productlines, on_delete=models.CASCADE)
    productVendor = models.CharField(default='', max_length=100)
    productDescription = models.TextField(default='')
    quantityInStock = models.IntegerField(default=0)
    image = models.ImageField(upload_to='Pictures')
    rentPrice = models.IntegerField(default=0)
    rate = models.IntegerField(default=0)

    def __str__(self):
        return self.productName


class variations(models.Model):
    product = models.ForeignKey(products, on_delete=models.CASCADE)
    title = models.CharField(default='', max_length=255)
    price = models.IntegerField(default=0)
    sale_price = models.IntegerField(default=0)
    inStock = models.IntegerField(default=0)


class promotions(models.Model):
    promoCode = models.CharField(default='', max_length=15)
    discount = models.IntegerField(default=0)
    startTime = models.DateTimeField(null=True, blank=True)
    endTime = models.DateTimeField(null=True, blank=True)
    description = models.TextField(default='')

    def __str__(self):
        return self.promoCode



