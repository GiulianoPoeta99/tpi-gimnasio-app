from django.db import models

from app.user.model import User
from app.trainer.models import Trainer
from app.rutine.model import Rutine

# Create your models here.
class AssingRutine(models.Model):
    user_id = models.ForeignKey(User , on_delete=models.RESTRICT)
    trainer_id = models.ForeignKey(Trainer , on_delete=models.RESTRICT)
    rutine_id = models.ForeignKey(Rutine , on_delete=models.RESTRICT)