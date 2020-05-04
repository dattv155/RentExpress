from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeview, name='home'),
    path('about/', views.aboutview, name='about'),
    path('product/', views.productview, name='product'),
    path('blog/', views.blogview, name='blog'),
    path('contact/', views.contactview, name='contact'),
    path('cart/', views.cartview, name='cart'),
    path('user/', views.userview, name='user'),
]