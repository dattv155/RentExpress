from django.contrib import admin
from .models import cart
from .models import cartItem

# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_display = ('user','create_at','update_at')
    search_fields = ('username',)


class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart','item','quantityOrdered','priceEach')
    search_fields = ('username',)


admin.site.register(cart, CartAdmin)
admin.site.register(cartItem, CartItemAdmin)