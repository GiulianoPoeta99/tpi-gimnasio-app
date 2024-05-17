from django.db import models
from app.rutine.model import Rutine
from app.exercise.models import Exercise

class RutineExercise(models.Model):
    rutine_id = models.ForeignKey(Rutine , on_delete=models.RESTRICT)
    exercise_id = models.ForeignKey(Exercise , on_delete=models.RESTRICT)