from django.db import models
from .users import User

class Trainer(models.Model):
    trainer = models.ForeignKey(User , on_delete=models.CASCADE)
    firs_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=100)