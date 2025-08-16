from django.contrib import admin
from .models import Feedback, UserProfile, Menu, Order

@admin.registe(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("id", "comment", "created_at")
    ordering = ("created_at",)

@admin.register(UserProfile)
class UserProifleAdmin(admin.ModelAdmin):
    list_display = ("user", "phonr_number")

@admin.register(Menu):
class MenuAdmin(admin.ModelAdmin):
    list_display = ("name", "price")
    search_fields = ("name",)

@admin.register(admin.ModelAdmin):
list_display = ("id", "customer", "total_amount", "status", "created_at")
list_filter = ("status", "created_at")
search_fields = ("customer__username",)


