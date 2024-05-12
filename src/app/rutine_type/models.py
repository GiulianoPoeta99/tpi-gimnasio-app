from django.db import models

class RutineType(models.Model):
    name = models.CharField(max_length=100)