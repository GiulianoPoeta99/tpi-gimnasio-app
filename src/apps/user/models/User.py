from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  pass
     
# AbstractUser es una clase de un framework para definir un modelo de usuario personalizado      
# Ya viene definido por defecto : (username, email, first_name, last_name, is_staff, is_active, etc.)