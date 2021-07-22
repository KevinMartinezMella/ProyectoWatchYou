from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Servidor, Usuario

# Create your views here.
def index(request):
    return render (request,'index.html')

def crear(request,data):
    if "id" in request.session:
        usuario = Usuario.objects.get(id = request.session['id'])
        servidor = Servidor(
            nombre_servidor=data['nombre'],
            ip=data['ip'],
            
        )
        servidor.save()
        servidor.usuario.add(usuario)


def update(request,idserver):
    get_server = Servidor.objects.get(id=idserver)
    edit_server = request.POST.get("servidor")
    edit_ip = request.POST.get("ip")
    get_server.nombre_servidor = edit_server
    get_server.ip = edit_ip
    get_server.save()

def delete(request,idserver):
    servidor = Servidor.objects.get(id=idserver)
    servidor.delete()