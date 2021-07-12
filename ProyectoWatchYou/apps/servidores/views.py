from django.shortcuts import redirect, render
from .models import Servidor
# Create your views here.
def index(request):
    return render (request,'index.html')

def crear(request,data):
    servidor = Servidor(
        nombre_servidor=data['nombre'],
        ip=data['ip'],
    )
    servidor.save()

def read(request):
    data = Servidor.objects.all()
    return data