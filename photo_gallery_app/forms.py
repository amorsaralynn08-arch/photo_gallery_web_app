from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import *


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label="Email Address",
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Enter your email"
        })
    )

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Enter your password"
        })
    )

    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Confirm your password"
        })
    )

    class Meta:
        model = User
        fields = ( "username","email")

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label="Email Address",
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Enter your email"
        })
    )

    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Enter your password"
        })
    )

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = [
            "bio",
            "profile_picture",
        ]

        widgets = {
            "bio": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Tell us about yourself..."
            }),
        }


class PhotoUploadForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = [
            "title",
            "description",
            "image",
            "tags",
        ]

        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Photo title"
            }),

            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Write a description..."
            }),

            "tags": forms.SelectMultiple(attrs={
                "class": "form-select"
            }),
        }