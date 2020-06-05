from django.contrib import admin

from manufacturer.models import Manufacturer


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


admin.site.register(Manufacturer, ManufacturerAdmin)