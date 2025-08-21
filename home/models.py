from django.db import models
from django.contrib.auth.models import User

class Feedback(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback {self.id} - {self.created_at.strftime('%y-%m-%d')}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Phone_number = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} - {self.phone_number or 'No phone'}"

class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.Price}";

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'pending'),
        ('confirmed', 'confirmed'),
        ('completed', 'completed'),
        ('cancelled', 'cancelled'),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Menu)
    total_Amount = models.DecimalField(max_digits=10, decimal+places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES), defult='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.customer.username} - {self.status}"

class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"




