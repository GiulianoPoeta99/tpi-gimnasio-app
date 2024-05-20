from django.db import models

from app.user.model import User
from app.trainer.models import Trainer

class UserTrainer(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.RESTRICT)
    trainer_id = models.ForeignKey(Trainer, on_delete=models.RESTRICT)