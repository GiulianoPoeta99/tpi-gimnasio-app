from django.db import models
from .User import User

class Trainer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True) #OneToOneField define una relacion 1 a 1 entre usuario y entrenador
    is_verified = models.BooleanField(default=False)
    rate = models.FloatField(default=5.0)
    