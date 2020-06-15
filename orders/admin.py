from django.contrib import admin

from orders.models import *


class DiscountAdmin(admin.ModelAdmin):
    list_display = ('promo_code', 'discount', 'start_time', 'end_time', 'description')
    search_fields = ('promo_code',)


class RentalAdmin(admin.ModelAdmin):
    list_display = ('customer', 'rental_start_time', 'rental_end_time', 'discount', 'description')
    search_fields = ('customer',)


class RentalDetailAdmin(admin.ModelAdmin):
    list_display = ('rental', 'vehicle', 'quantity', 'price_each')
    search_fields = ('rental',)


admin.site.register(Discount, DiscountAdmin)
admin.site.register(Rental, RentalAdmin)
admin.site.register(RentalDetail, RentalDetailAdmin)
