from django.db import models
from django.db.models.base import Model

# Create your models here.
class Servidor(models.Model):
    nombre_servidor = models.CharField(max_length=255,null=False,blank=False)
    ip = models.CharField(max_length=255,null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.ip}'