from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import FormView

from vehicles.models import Vehicle
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
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
    paginator = Paginator(object_list, 4)
    page_number = request.GET.get('page')
    try:
        list_vehicle = paginator.page(page_number)
    except PageNotAnInteger:
        list_vehicle = paginator.page(1)
    except EmptyPage:
        list_vehicle = paginator.page(paginator.num_pages)
    context = {'list_vehicle': list_vehicle, 'my_filter': my_filter, 'nav': 'vehicle'}

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


def blog1_view(request):
    return render(request, 'blog-1.html', {
        'nav': 'blog'
    })


def blog2_view(request):
    return render(request, 'blog-2.html', {
        'nav': 'blog'
    })


def blog3_view(request):
    return render(request, 'blog-3.html', {
        'nav': 'blog'
    })


def contact_view(request):
    return render(request, 'contact.html', {
        'nav': 'contact'
    })


def booking_view(request):
    return render(request, 'booking.html')


def booking_cart(request):
    html = 'Successfully booking'
    if request.is_ajax():
        id = request.POST.get('id')
        num = request.POST.get('num')

        html = render_to_string('booking.html')
    return HttpResponse(html)

