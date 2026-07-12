from django.contrib import admin
from .models import Profile, Tag, Photo

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "created_at",
        "updated_at",
    )

    search_fields = (
        "user__username",
        "user__email",
    )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        "name",
    )

    search_fields = (
        "name",
    )


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "user",
        "total_likes",
        "total_dislikes",
        "created_at",
    )

    list_filter = (
        "tags",
        "created_at",
    )

    search_fields = (
        "title",
        "description",
        "user__username",
    )

    filter_horizontal = (
        "tags",
        "likes",
        "dislikes",
    )