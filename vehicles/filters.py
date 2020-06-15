from django_filters import *

from .models import *


class VehicleBaseFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Vehicle
        fields = ['name']


class VehicleFilter(FilterSet):
    price = RangeFilter(field_name='rent_price')

    class Meta:
        model = Vehicle
        fields = ['vehicle_line', 'manufacturer', 'hire_point', 'price']

