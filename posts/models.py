"""Posts models."""

# Django 
from django.db import models


class User(models.Model):
    """User model."""

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    is_admin = models.BooleanField(default=False)

    bio = models.TextField(blank=True)

    birthdate = models.DateField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True) # <-- "auto_now_add" es como GETDATE() cuando se crea
    modified = models.DateTimeField(auto_now=True) # <-- "auto_now" es como GETDATE() cada vez que se modifica

    country = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)

    def __str__(self):
        """Return emal."""
        return self.email