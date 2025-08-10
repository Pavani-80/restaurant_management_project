from django.shortcuts import render
from django.conf import settings 

def custom_404(request, exception):
    return render(request, '404.html', status=404)

def home_view(request):
    context = { 
        'restaurant_name': settings.RESTAURANT_NAME,
        'restaurant_phone': settings.RESTAURANT_PHONE
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    contact_info = {
        "phone": "+91 98765 43210",
        "email": "info@myrestaurant.com",
        "address": "123 Main Street, Hyderabad, India"
    }
    return render(request, "contact.html, {"contact_info": contact_info})

def reservations(request):
    return render(request, 'reservations.html')
