from django.shortcuts import render

from vehicles.models import Vehicle


def home_view(request):
    return render(request, 'index.html', {
        'nav': 'home'
    })


def about_view(request):
    return render(request, 'about.html', {
        'nav': 'about'
    })


def vehicle_view(request):
    object_list = Vehicle.objects.all()
    return render(request, 'car.html', {
        'object_list': object_list,
        'nav': 'vehicle'
    })


def blog_view(request):
    return render(request, 'blog.html', {
        'nav': 'blog'
    })


def contact_view(request):
    return render(request, 'contact.html', {
        'nav': 'contact'
    })

