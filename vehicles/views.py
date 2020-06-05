from django.shortcuts import render

from vehicles.models import Vehicle


def home_view(request):
    # return render(request, 'index.html', {
    #    'nav': 'home'
    #})

    return render(request, 'index.html')


def about_view(request):
    return render(request, 'about.html')


def vehicle_view(request):
    object_list = Vehicle.objects.all()
    return render(request, 'car.html', {
        'object_list': object_list
    })


def blog_view(request):
    return render(request, 'blog.html')


def contact_view(request):
    return render(request, 'contact.html')


def login_view(request):
    return render(request, 'login.html')
