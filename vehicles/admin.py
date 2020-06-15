from django.contrib import admin

from vehicles.models import Vehicle, VehicleLine, Manufacturer, HirePoint


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


class VehicleLineAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


class HirePointAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'address_line1', 'address_line2', 'address_line3', 'description' )
    search_fields = ('name',)


class VehicleAdmin(admin.ModelAdmin):
    list_display = ('name', 'vehicle_line', 'manufacturer', 'quantity', 'rent_price', 'rating')
    search_fields = ('name',)


admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(VehicleLine, VehicleLineAdmin)
admin.site.register(HirePoint, HirePointAdmin)
admin.site.register(Vehicle, VehicleAdmin)
