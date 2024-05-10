from django.db import models
from .User import User
from .Trainer import Trainer

class UserTrainer(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, null=True) #ForeignKey representa relacion muchos a uno
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, null=True)