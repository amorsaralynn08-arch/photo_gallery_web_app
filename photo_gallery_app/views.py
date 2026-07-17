from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile, Tag
from django.shortcuts import get_object_or_404
import requests


from .forms import (
    CustomUserCreationForm,
    CustomAuthenticationForm,
    ProfileUpdateForm,
    PhotoUploadForm,
)

from .models import Photo


def index(request):

    photos = Photo.objects.all().order_by("-created_at")

    search = request.GET.get("search")

    if search:
        photos = photos.filter(
            title__icontains=search
        )

    tags = Tag.objects.all()

    return render(
        request,
        "dashboard.html",
        {
            "photos": photos,
            "tags": tags,
        }
    )

def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully.")
            return redirect("index")
    else:
        form = CustomUserCreationForm()

    return render(request, "registration.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("index")
    else:
        form = CustomAuthenticationForm()

    return render(request, "login.html", {"form": form})


@login_required
def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    return render(request, "profile.html", {
        "profile": profile
    })




from .models import Profile

@login_required
def update_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":

        request.user.username = request.POST.get("username")
        request.user.email = request.POST.get("email")
        request.user.save()

        profile.bio = request.POST.get("bio")

        if request.FILES.get("profile_picture"):
            profile.profile_picture = request.FILES["profile_picture"]

        profile.save()

        messages.success(request, "Profile updated successfully!")

        return redirect("profile")

    return redirect("profile")

def photo_detail(request, pk):
    photo = Photo.objects.get(id=pk)

    return render(
        request,
        "photo_detail.html",
        {"photo": photo},
    )


@login_required
def like_photo(request, pk):

    photo = get_object_or_404(Photo, id=pk)

    photo.likes.add(request.user)

    return redirect("index")


@login_required
def dislike_photo(request, pk):

    photo = get_object_or_404(Photo, id=pk)

    photo.dislikes.add(request.user)

    return redirect("index")


def filter_by_tag(request, tag):
    photos = Photo.objects.filter(tags__name=tag)

    return render(
        request,
        "dashboard.html",
        {"photos": photos},
    )

@login_required
def edit_photo(request, pk):

    photo = get_object_or_404(Photo, id=pk, user=request.user)

    if request.method == "POST":
        form = PhotoUploadForm(
            request.POST,
            request.FILES,
            instance=photo
        )

        if form.is_valid():
            form.save()
            return redirect("index")

    else:
        form = PhotoUploadForm(instance=photo)

    return render(request, "edit_photo.html", {
        "form": form
    })


@login_required
def delete_photo(request, pk):

    photo = get_object_or_404(Photo, id=pk, user=request.user)

    if request.method == "POST":
        photo.delete()
        return redirect("index")

    return render(request, "delete_photo.html", {
        "photo": photo
    })
@login_required
def upload_photo(request):
    if request.method == "POST":
        form = PhotoUploadForm(request.POST, request.FILES)

        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            form.save_m2m()
            return redirect("index")
    else:
        form = PhotoUploadForm()

    return render(request, "upload_photo.html", {"form": form})