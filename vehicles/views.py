from django.shortcuts import render
from django.urls import reverse
from django.views.generic import FormView

from vehicles.models import Vehicle
from .filters import *


def home_view(request):
    context = {'nav': 'home'}
    return render(request, 'index.html', context)


def about_view(request):
    return render(request, 'about.html', {
        'nav': 'about'
    })


def vehicle_view(request):
    object_list = Vehicle.objects.all()

    my_filter = VehicleFilter(request.GET, queryset=object_list)
    object_list = my_filter.qs

    if 'input' in request.GET and request.GET['input']:
        word = request.GET['input']
        object_list = Vehicle.objects.filter(name__icontains=word)

    context = {'object_list': object_list, 'my_filter': my_filter, 'nav': 'vehicle'}

    return render(request, 'car.html', context)


def vehicle_single_view(request):
    name_vehicle = request.GET.get('vehicle_single')
    vehicle = Vehicle.objects.get(name=name_vehicle)
    vehicle.save()

    context = {'vehicle': vehicle, 'nav': 'vehicle'}

    return render(request, 'vehicle-single.html', context)


def blog_view(request):
    return render(request, 'blog.html', {
        'nav': 'blog'
    })


def contact_view(request):
    return render(request, 'contact.html', {
        'nav': 'contact'
    })

