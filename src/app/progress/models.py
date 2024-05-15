from django.db import models
from app.user.models import User
from app.exercise.models import Exercise

class Progress(models.Model):
    id_user = models.OneToOneField(User,on_delete=models.RESTRICT)
    id_exercise = models.ForeignKey(Exercise,on_delete=models.RESTRICT)
    weight = models.FloatField()
    repetitions = models.IntegerField()