"""
URL configuration for ecomm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from cart import views
app_name='cart'
urlpatterns = [
     path('add_to_cart/<int:i>/',views.add_to_cart,name="add_to_cart"),
     path('cart_view/',views.cart_view, name='viewcart'),
     path('cart_decrement/<int:i>',views.cart_decrement, name='cart_decrement'),
     path('cart_delete<int:i>',views.remove, name='cart_delete'),
     path('order',views.order,name='order'),
     path('status/<u>',views.payment_status,name='status'),
     path('yourorders/',views.yourorders,name='yourorders'),


]

if settings.DEBUG:
     urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)