from django.shortcuts import render
from django.conf import settings 
from django.http import HttpResponse
from django.db import DatabaseError
from datetime import datetime

def custom_404(request, exception):
    return render(request, '404.html', status=404)
        }
def home_view(request):
    try:
        context = { 
            'restaurant_name': settings.RESTAURANT_NAME,
            'restaurant_phone': settings.RESTAURANT_PHONE,
            'current_year': datetime.now().year
    }
        return render(request, 'home.html', context)
    except DatabaseError:
        return HttpResponse("Sorry, we are having technical issues with our database.", status=500)
    except Exception as e:
        return HttpResponse(f"An unexpected error occured: {e}", status=500)

def about(request):
    return render(request, 'about.html')

def contact(request):
    contact_info = {
        "phone": "+91 98765 43210",
        "email": "info@myrestaurant.com",
        "address": "123 Main Street, Hyderabad, India"
    }
    return render(request, "contact.html", {"contact_info": contact_info})

def reservations(request):
    return render(request, 'reservations.html', {'current_year': datetime.now().year})
        
