from django.db import models
from django.forms import ValidationError
from app.user.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

def _validate_one_to_five(value):
    if value < 1 or value > 5:
        raise ValidationError('El valor debe estar entre 1 y 5')

class Trainer(models.Model):
    user_id = models.ForeignKey(User , on_delete=models.RESTRICT)
    is_verify = models.BooleanField(models.BooleanField(default=False))
    rate = models.IntegerField(
        validators=[_validate_one_to_five, MinValueValidator(1), MaxValueValidator(5)],
        verbose_name='Rate'
    )