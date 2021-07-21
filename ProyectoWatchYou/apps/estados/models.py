from os import name
from django.db import models
from apps.servidores.models import Servidor

# Create your models here.
class Estado(models.Model):
    estado = models.CharField(max_length=255,blank=False,null=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # servidor = models.ForeignKey(Servidor,related_name="estado",on_delete=models.CASCADE)
    estados_servidores = models.ManyToManyField(Servidor, through='EstadoServidor')
    def __repr__(self):
        return self.estado

class EstadoServidor(models.Model):
    fechahora = models.DateTimeField(auto_now_add=True)
    servidores = models.ForeignKey(Servidor, related_name="estados", on_delete=models.CASCADE)
    estados = models.ForeignKey(Estado, related_name="servidores", on_delete=models.CASCADE)