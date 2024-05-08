from django.db import models
from .user import User

class UserTrainer(models.Model):
    user_trainer = models.ForeignKey( User, on_delete=models.CASCADE)
    firs_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)