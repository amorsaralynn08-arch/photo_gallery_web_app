from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("registration/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),

    path("profile/", views.profile, name="profile"),
    path("profile/update/", views.update_profile, name="update_profile"),

    path("upload/", views.upload_photo, name="upload_photo"),

    path("photo/<int:pk>/", views.photo_detail, name="photo_detail"),

    path("photo/<int:pk>/like/", views.like_photo, name="like_photo"),
    path("photo/<int:pk>/dislike/", views.dislike_photo, name="dislike_photo"),

    path("tag/<str:tag>/", views.filter_by_tag, name="filter_by_tag"),
    path("photo/<int:pk>/edit/", views.edit_photo, name="edit_photo"),
    path("photo/<int:pk>/delete/", views.delete_photo, name="delete_photo"),
]