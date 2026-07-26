# forms.py
from django import forms
from .models import Signup
from django.contrib.auth.models import User

class SignupForm(forms.ModelForm):
    class Meta:
        model = Signup
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "message",
        ]

        widgets = {
            "username": forms.TextInput(attrs={
                "class": "w-full bg-[#1b1b1b] border border-gray-700 rounded-xl px-5 py-4 text-white",
                "placeholder": "Enter username",
            }),
            "first_name": forms.TextInput(attrs={
                "class": "w-full bg-[#1b1b1b] border border-gray-700 rounded-xl px-5 py-4 text-white",
                "placeholder": "Enter first name",
            }),
            "last_name": forms.TextInput(attrs={
                "class": "w-full bg-[#1b1b1b] border border-gray-700 rounded-xl px-5 py-4 text-white",
                "placeholder": "Enter last name",
            }),
            "email": forms.EmailInput(attrs={
                "class": "w-full bg-[#1b1b1b] border border-gray-700 rounded-xl px-5 py-4 text-white",
                "placeholder": "Enter email",
            }),
            "password": forms.PasswordInput(attrs={
                "class": "w-full bg-[#1b1b1b] border border-gray-700 rounded-xl px-5 py-4 text-white",
                "placeholder": "Enter password",
            }),
            "message": forms.Textarea(attrs={
                "class": "w-full bg-[#1b1b1b] border border-gray-700 rounded-xl px-5 py-4 text-white resize-none",
                "rows": 5,
                "placeholder": "Write your message",
            }),
        }
