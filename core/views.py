from django.shortcuts import render
from product.models import products

# Create your views here.


def homeview(request):
    return render(request, 'homepage/index.html', {
        'nav': 'home'
    })


def aboutview(request):
    return render(request, 'homepage/about.html', {
        'nav': 'about'
    })


def productview(request):
    object_list = products.objects.filter()
    return render(request, 'homepage/car.html', {
        'object_list': object_list,
        'nav': 'product'
    })


def blogview(request):
    return render(request, 'homepage/blog.html', {
        'nav': 'blog'
    })


def contactview(request):
    return render(request, 'homepage/contact.html', {
        'nav': 'contact'
    })


def cartview(request):
    return render(request, 'homepage/cart.html', {
        'nav': 'cart'
    })


def userview(request):
    return render(request, 'homepage/user.html', {
        'nav': 'user'
    })

