from django.contrib import admin
from .models import orders
from .models import shipping

# Register your models here.


class OrdersAdmin(admin.ModelAdmin):
    list_display = ('user','cart','is_shipping','description','totalPrice','is_rented','is_completed')
    search_fields = ('user',)


class ShippingAdmin(admin.ModelAdmin):
    list_display = ('order','address','orderDate','requiredDate','shippedDate','status','description')
    search_fields = ('order',)


admin.site.register(orders, OrdersAdmin)
admin.site.register(shipping, ShippingAdmin)