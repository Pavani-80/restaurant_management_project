from django.shortcuts import render,redirect
from django.conf import settings 
from django.http import HttpResponse
from django.db import DatabaseError
from datetime import datetime
from .models import Feedback, MenuItem, Restaurant
import requests

def custom_404(request, exception):
    return render(request, '404.html', status=404)
        }
def home_view(request):
    try:
        menu_items = MenuItem.objects.all()
        try:
            response = requests.get("http://127.0.0.1:8000/api/menu")
            if response.status_code == 200:
                menu_items = response.json()
            else:
                menu_items = []
        except:
            menu_items = []

        restaurant = Restaurant.objects.first()

        context = { 
            'restaurant_name': restaurant.name if restaurant else settings.RESTAURANT_NAME,
            'restaurant_phone': restaurant.phone if restaurant else settings.RESTAURANT_PHONE,
            'restaurant_email': restaurant.email if restaurant else "info@myrestaurant.com"
            'restaurant_address': restaurant.address if restaurant else "123 Food street, Banglore, India"
            'current_year': datetime.now().year
            'menu_items': menu_items,
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
        "address": "123 Main Street, Banglore, India"
    }
    return render(request, "contact.html", {"contact_info": contact_info})

def reservations(request):
    return render(request, 'reservations.html', {'current_year': datetime.now().year})

def feedback_view(request):
    if request.method == "POST":
        comment = request.POST.get("comment")
        if comment:
          Feedback.objects.create(comment=comment)
          return redirect("feedback")
    feedback_list = Feedback.objects.all().order_by('-created_at')
    return render(request, "feedback.html", {"feedback_list": feedback_list"})
        
