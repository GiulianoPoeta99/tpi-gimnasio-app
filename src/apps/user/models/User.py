from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  username = models.CharField(max_length=150, unique=True, null=True, blank=True)
  email = models.EmailField(unique=True, null=True, blank=True)
  password = models.CharField(max_length=128, null=True, blank=True)  # Django almacena las contraseñas hash
  profile_picture = models.ImageField(upload_to='profiles/', blank=True , null=True)
     
# AbstractUser es una clase de un framework para definir un modelo de usuario personalizado      
# Ya viene definido por defecto : (username, email, first_name, last_name, is_staff, is_active, etc.)