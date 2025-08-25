from django.contrib import admin
from .models import Feedback, UserProfile, Menu, Order
from .models import MenuItem

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("id", "comment", "created_at")
    ordering = ("created_at",)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "phone_number")

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("name", "price")
    search_fields = ("name",)

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("name", "menu", "price")
    search_fields = ("name")

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "total_amount", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("customer__username",)

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "email", "address")


