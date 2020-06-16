from django.shortcuts import render
from django.urls import reverse
from django.views.generic import FormView

from vehicles.models import Vehicle
from .filters import *


def home_view(request):
    '''object_list = Vehicle.objects.all()

    my_base_filter = VehicleBaseFilter(request.GET, queryset=object_list)
    object_list = my_base_filter.qs

    context = {'object_list': object_list, 'my_base_filter': my_base_filter, 'nav': 'home'}'''

    context1 = {'nav': 'home'}
    submit_button = request.GET.get('vehicle')
    if submit_button == 'Search':
        query = request.GET.get('input')
        if query is not None:
            results = Vehicle.objects.filter(name__icontains=query)

            # filter all the product which title and content has word in query in category table
            context = {'nav': 'home',
                       'results': results,
                       'submit_button': submit_button}

            return render(request, 'car.html', context)
        else:
            return render(request, 'car.html', context1)
    else:
        return render(request, 'index.html', context1)


def about_view(request):
    return render(request, 'about.html', {
        'nav': 'about'
    })


def vehicle_view(request):
    object_list = Vehicle.objects.all()

    my_filter = VehicleFilter(request.GET, queryset=object_list)
    object_list = my_filter.qs

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

