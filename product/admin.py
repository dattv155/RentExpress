from django.contrib import admin
from .models import products
from .models import productlines
# Register your models here.


class ProductlinesAdmin(admin.ModelAdmin):
    list_display = ('productLineName', 'description')
    search_fields = ('productLineName',)


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('productName','productLine','productVendor','productDescription',
                    'quantityInStock','image','rentPrice','rate')
    search_fields = ('productName',)


admin.site.register(productlines, ProductlinesAdmin)
admin.site.register(products, ProductsAdmin)
