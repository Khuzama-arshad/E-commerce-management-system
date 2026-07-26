from django.urls import path
from . import views
urlpatterns = [
    path('', views.Cart, name='cart'),
    path("cart/add/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
]
