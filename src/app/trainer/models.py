from django.db import models
from app.user.models import User

class Trainer(models.Model):
    user_id = models.ForeignKey(User , on_delete=models.RESTRICT)
    is_verify = models.BooleanField(models.BooleanField(default=False))
    rate = models.IntegerField()