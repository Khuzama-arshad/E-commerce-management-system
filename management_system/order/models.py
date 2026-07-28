from django.db import models
from django.contrib.auth.models import User
from product.models import Product
# Create your models here.
class Order(models.Model):
    STATUS_CHOICES = [
         ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # Shipping Details 
    user_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    city = models.CharField(max_length=40)

    def __str__(self):
        return f"Order # {self.id} - {self.user.username} - {self.status}"
    def calculate_total_price(self):
        self.total_price = sum((item.get_total()) for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name = "items")
    product = models.ForeignKey('product.Product' , on_delete=models.CASCADE )
    quantity = models.PositiveIntegerField(default=1)
    def get_total(self):
        return self.product.price * self.quantity