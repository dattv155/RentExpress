from django.contrib import admin
from .models import products
from .models import productlines
from .models import promotions
from .models import variations

# Register your models here.


class ProductlinesAdmin(admin.ModelAdmin):
    list_display = ('productLineName', 'description')
    search_fields = ('productLineName',)


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('productName','productLine','productVendor','productDescription',
                    'quantityInStock','image','rentPrice','rate')
    search_fields = ('productName',)


class VariationsAdmin(admin.ModelAdmin):
    list_display = ('product','title','price','sale_price','inStock')
    search_fields = ('promoCode',)


class PromotionAdmin(admin.ModelAdmin):
    list_display = ('promoCode','discount','startTime','endTime','description')
    search_fields = ('productName',)


admin.site.register(productlines, ProductlinesAdmin)
admin.site.register(products, ProductsAdmin)
admin.site.register(variations, VariationsAdmin)
admin.site.register(promotions, PromotionAdmin)
