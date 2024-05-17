from django.db import models
from django.core.exceptions import ValidationError

from app.user.models import User
from app.difficulty_level.models import DifficultyLevel
from app.rutine_type.models import RutineType
from .manager import RutineManager

class Rutine(models.Model):
    name = models.CharField(max_length=60)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    difficulty_level = models.OneToOneField(DifficultyLevel, on_delete=models.RESTRICT, null=True)
    rutine_type = models.ManyToManyField(RutineType)

    objects = RutineManager()

    def __str__(self):
        return self.name

    def clean(self):
        if self.difficulty_level is None:
            raise ValidationError("Debe especificar un nivel de dificultad para la rutina.")

    class Meta:
        verbose_name = "Rutina"
        verbose_name_plural = "Rutinas"
        ordering = ['name']
