from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    bio = models.TextField(
        blank=True,
        null=True
    )

    profile_picture = CloudinaryField(
        "profile_picture",
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.user.username


class Tag(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True
    )

    def __str__(self):
        return self.name


class Photo(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="photos"
    )

    title = models.CharField(
        max_length=200
    )

    description = models.TextField()

    image = CloudinaryField(
        "image"
    )

    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name="photos"
    )

    likes = models.ManyToManyField(
        User,
        blank=True,
        related_name="liked_photos"
    )

    dislikes = models.ManyToManyField(
        User,
        blank=True,
        related_name="disliked_photos"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def total_likes(self):
        return self.likes.count()

    def total_dislikes(self):
        return self.dislikes.count()

    def __str__(self):
        return self.title