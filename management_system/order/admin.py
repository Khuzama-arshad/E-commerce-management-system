# your_app/admin.py
from django.contrib import admin
from .models import Order, OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_name', 'email', 'phone', 'status', 'total_price', 'created_at']
    list_filter = ['status', 'city']
    search_fields = ['user_name', 'email', 'phone']

admin.site.register(OrderItem)