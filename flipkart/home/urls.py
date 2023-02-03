from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.index,name='Home'),
    path('grocery', views.grocery,name='grocery'),
    path('mobiles', views.mobiles,name='mobiles'),
    path('fashion', views.fashion,name='fashion'),
    path('electronics', views.electronics,name='electronics'),
    path('appliances', views.appliances,name='appliances'),
    path('travel', views.travel,name='travel'),
    path('topoffer', views.topoffer,name='topoffer'),
    path('beauty', views.beauty,name='beauty'),
] 