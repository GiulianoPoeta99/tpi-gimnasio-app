from django.contrib.auth.models import AbstractUser
# Modelo predeterminado de usuario de Django
from django.db import models
from app.user.manager import CustomUserManager

class User(AbstractUser):
    username = None #Se elimina el campo username ya que no se usa
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email' #Identifica que el email sera el campo unico para identificar a los usuarios
    REQUIRED_FIELDS = ['first_name', 'last_name'] #Agrega campos obligatorios para crear un superusuario (ademas del email y pass)
    
    trainers = models.ManyToManyField('self', symmetrical=False, related_name='user_trainer') ## relacion n a n entre usuarios y entrenadores

    objects = CustomUserManager() # Definde el administrador del modelo

    def __str__(self):
        return self.email
