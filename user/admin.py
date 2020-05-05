from django.contrib import admin
from .models import CustomerUser

# Register your models here.


class CustomerUserAdmin(admin.ModelAdmin):
    list_display = ('username','first_name','last_name','email','phone_number','address')
    search_fields = ('username',)


admin.site.register(CustomerUser, CustomerUserAdmin)