from django.db import models

from .manager import MuscleExerciseManager

class MuscleExercise (models.Model):
    name = models.CharField(max_length=100)

    objects = MuscleExerciseManager

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "ejercicio de musculo"
        verbose_name_plural = "ejercicios de musculos"
        ordering = ['name']
