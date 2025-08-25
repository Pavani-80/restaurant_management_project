from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu_list, name='menu_list'),
    path('contact/', views.contact, name='contact'),
    path('reservations/', views.reservations, name='reservations'),
    path("", include("yourapp.urls")),
]