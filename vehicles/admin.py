from django.contrib import admin

from vehicles.models import Vehicle


class VehicleAdmin(admin.ModelAdmin):
    list_display = ('name', 'manufacturer', 'quantity', 'rent_price', 'rating')
    search_fields = ('name',)


admin.site.register(Vehicle, VehicleAdmin)