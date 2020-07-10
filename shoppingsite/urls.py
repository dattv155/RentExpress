"""shoppingsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from vehicles import views
from profiles import views as profiles_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('vehicle/', views.vehicle_view, name='vehicle'),
    path('vehicle_single/', views.vehicle_single_view, name='vehicle_single'),
    path('blog/', views.blog_view, name='blog'),
    path('blog/1', views.blog1_view, name='blog-1'),
    path('blog/2', views.blog2_view, name='blog-2'),
    path('blog/3', views.blog3_view, name='blog-3'),
    path('contact/', views.contact_view, name='contact'),
    path('booking/', views.booking_view, name='booking'),

    #path('accounts/', include('django.contrib.auth.urls')),
    path('login/', profiles_views.SiteLoginView.as_view(), name='login'),
    path('register/', profiles_views.RegisterView.as_view(), name='register'),
    path('register_ok/', profiles_views.RegisterOkView.as_view(), name='register_ok'),
    path('logout/', profiles_views.SiteLogoutView.as_view(), name='logout'),
    path('profile/', profiles_views.ProfileEditView.as_view(), name='profile'),

    #path('booking/', views.booking_cart, name='booking_cart')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


