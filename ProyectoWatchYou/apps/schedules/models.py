from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, DateTimeField, TimeField
from apps.servidores.models import Servidor
from django.db import models

# Create your models here.
class Schedule(models.Model):
    idserver = models.ForeignKey(Servidor, related_name="idservidor", on_delete=models.CASCADE)
    hora = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.hora}"