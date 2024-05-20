from django.db import models

from app.user.model import User
from app.rutine.model import Rutine

class PickRutine(models.Model):
    user_id = models.ForeignKey(User , on_delete=models.RESTRICT)
    Rutine_id = models.ForeignKey(Rutine , on_delete=models.RESTRICT)