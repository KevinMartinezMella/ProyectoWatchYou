from django.db import models
from apps.servidores.models import Servidor

# Create your models here.
class Estado(models.Model):
    estado = models.CharField(max_length=255,blank=False,null=False)
    fecha_hora = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    servidor = models.ForeignKey(Servidor,related_name="estado",on_delete=models.CASCADE)