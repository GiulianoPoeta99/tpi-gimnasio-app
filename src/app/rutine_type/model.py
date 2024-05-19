from django.db import models

class RutineType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Tipo de rutina"
        verbose_name_plural = "Tipos de rutina"
        ordering = ['name']