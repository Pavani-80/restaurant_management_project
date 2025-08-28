from django.conf import settings
from django.conf.urls.sattic import sattic
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu_list, name='menu_list'),
    path('contact/', views.contact, name='contact'),
    path('reservations/', views.reservations, name='reservations'),
    path('admin/', admin.site.urls),
    path('', include("yourapp.urls")),
    path('products/', include('products.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)