from django.urls import path
from . import views
urlpatterns = [
    path("signup/", views.Signup, name="signup"),     # http://127.0.0.1:8000/
    path("login/", views.Login, name="login"),
    path("logout/", views.Logout, name="logout"),
]
