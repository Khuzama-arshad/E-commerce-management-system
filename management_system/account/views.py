from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def Signup(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        # Password check
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("signup")

        # Username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("signup")

        # Email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect("signup")

        # Create user
        User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password,
        )

        messages.success(request, "Account created successfully.")
        return redirect("login")

    return render(request, "signup.html")

def Login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome, {user.username}!")
            return redirect("/")      # Change to your home page

        else:
            messages.error(request, "Invalid username or password.")
            return redirect("login")

    return render(request, "login.html")

def Logout(request):
    logout(request)
    return redirect('login')