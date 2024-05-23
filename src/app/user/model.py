from django.contrib.auth.models import AbstractUser
from django.db import models
from app.user.manager import CustomUserManager  # Asegúrate de que la ruta sea correcta

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
