from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from django.db import DatabaseError
from datetime import datetime
from .models import Feedback, Menu
from rest_framework.decorators import api_view
from rest_framework.response import Response


# ==============================
# Custom Error Handler
# ==============================
def custom_404(request, exception):
    return render(request, "404.html", status=404)


# ==============================
# Home Page
# ==============================
def home_view(request):
    try:
        menu_items = Menu.objects.all()  # fetch directly from DB

        context = {
            "restaurant_name": getattr(settings, "RESTAURANT_NAME", "Hungry Vibes"),
            "restaurant_phone": getattr(settings, "RESTAURANT_PHONE", "+91 9876543210"),
            "restaurant_email": getattr(settings, "RESTAURANT_EMAIL", "hungryvibes@gmail.com"),
            "restaurant_address": getattr(settings, "RESTAURANT_ADDRESS", "123 Food Street, Hyderabad, India"),
            "current_year": datetime.now().year,
            "menu_items": menu_items,
        }
        return render(request, "home.html", context)

    except DatabaseError:
        return HttpResponse("Sorry, we are having technical issues with our database.", status=500)
    except Exception as e:
        return HttpResponse(f"An unexpected error occurred: {e}", status=500)


# ==============================
# About Page
# ==============================
def about(request):
    context = {
        "restaurant_name": settings.RESTAURANT_NAME,
        "restaurant_phone": settings.RESTAURANT_PHONE,
        "restaurant_email": settings.RESTAURANT_EMAIL,
        "restaurant_address": settings.RESTAURANT_ADDRESS,
        "current_year": datetime.now().year,
    }
    return render(request, "about.html", context)


# ==============================
# Contact Page
# ==============================
def contact(request):
    contact_info = {
        "name": settings.RESTAURANT_NAME,
        "phone": settings.RESTAURANT_PHONE,
        "email": settings.RESTAURANT_EMAIL,
        "address": settings.RESTAURANT_ADDRESS,
    }
    context = {
        "contact_info": contact_info,
        "current_year": datetime.now().year,
    }
    return render(request, "contact.html", context)


# ==============================
# Reservations Page
# ==============================
def reservations(request):
    context = {
        "restaurant_name": settings.RESTAURANT_NAME,
        "restaurant_phone": settings.RESTAURANT_PHONE,
        "restaurant_email": settings.RESTAURANT_EMAIL,
        "restaurant_address": settings.RESTAURANT_ADDRESS,
        "current_year": datetime.now().year,
    }
    return render(request, "reservations.html", context)


# ==============================
# Feedback Page
# ==============================
def feedback_view(request):
    if request.method == "POST":
        comment = request.POST.get("comment")
        if comment:
            Feedback.objects.create(comment=comment)
            return redirect("feedback")

    feedback_list = Feedback.objects.all().order_by("-created_at")

    context = {
        "feedback_list": feedback_list,
        "restaurant_name": settings.RESTAURANT_NAME,
        "restaurant_phone": settings.RESTAURANT_PHONE,
        "restaurant_email": settings.RESTAURANT_EMAIL,
        "restaurant_address": settings.RESTAURANT_ADDRESS,
        "current_year": datetime.now().year,
    }
    return render(request, "feedback.html", context)


# ==============================
# API Endpoint for Menu
# ==============================
@api_view(["GET"])
def menu_list(request):
    menu_items = Menu.objects.all().values("id", "name", "description", "price")
    return Response(list(menu_items))

        

