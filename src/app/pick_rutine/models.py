from django.db import models
from app.user.models import User
from app.rutine.models import Rutine

class PickRutine(models.Model):
    user_id = models.ForeignKey(User , on_delete=models.RESTRICT)
    Rutine_id = models.ForeignKey(Rutine , on_delete=models.RESTRICT)