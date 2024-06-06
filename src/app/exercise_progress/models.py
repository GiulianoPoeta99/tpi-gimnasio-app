from django.db import models

from app.exercise.model import Exercise
from app.user.model import User


class ExerciseProgress(models.Model):
    id_user = models.ForeignKey(User,on_delete=models.RESTRICT)
    id_exercise = models.ForeignKey(Exercise,on_delete=models.RESTRICT)
