from django.db import models
from apps.usuarios.models import Usuario
# Create your models here.
class Licencia(models.Model):
    licencia = models.CharField(max_length=255,blank=False,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(Usuario,related_name="usuario",on_delete=models.CASCADE)