from apps.estados.models import EstadoServidor,Estado
from django.http import request
from django.shortcuts import redirect, render
from apps.usuarios.models import Usuario
from apps.servidores.views import crear,update,delete
from apps.clases.monitor import Monitor, Validar
from apps.schedules.models import *
from apps.schedules.views import agregarSchedule
from datetime import datetime, timezone
import threading
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    if request.method == "GET":
        return render(request,'index.html')
    elif request.method == "POST":
        try:
            usuario = Usuario.objects.get(email=request.POST['email'])
        except:
            usuario = None
        if usuario and usuario.password == request.POST['pw']:
            request.session['id'] = usuario.id
            request.session['usuario'] = usuario.email
            request.session['nombre'] = usuario.nombre
            return redirect("/dashboard")
        else:
            return redirect("/")

def dashboard(request):
    if request.method == "GET" and "usuario" in request.session:
        usuario_actual = request.session["nombre"]
        user_actual = usuario_actual.upper()
        usuario = Usuario.objects.get(id = request.session['id'])
        estados = EstadoServidor.objects.all()
        data = []        
        for estado in estados:
            data.append(estado.estados)
        context = {
            "usuario_actual": user_actual,
            "servers": usuario.servidores.all(),
            "estados": data,
            "estadisticas": estados
        }
        return render(request, 'dashboard.html', context)
    else:
        return redirect("/")

def devices(request):
    if request.method == "GET" and "usuario" in request.session:
        usuario_actual = request.session["nombre"]
        usuario = Usuario.objects.get(id = request.session['id'])
        user_actual = usuario_actual.upper()
        context = {
            "usuario_actual": user_actual,
            "servers": usuario.servidores.all(),

        }
        return render(request,'devices.html', context)
    else:
        return redirect("/")

def nuevo_srv(request):
    context={
        "nombre":request.POST['servidor'],
        "ip":request.POST['ip']
    }
    crear(request,context)
    return redirect("/devices")

def erase(request,idserver):
    if request.method=="POST":
        delete(request,idserver)
        return redirect("/devices")
    idserv = idserver
    context = {
        "idserv":idserv
    }   
    return render(request,'eliminarServidor.html',context)

def edit(request,idserver):
    data = update(request,idserver)
    return redirect('/devices')


def probar(idserver):
    monitor = Monitor()
    isUp = monitor.ping(idserver)
    validar = Validar()
    validar.verificar(isUp)

def multiThread(request,delay=0):
    task = threading.Timer(delay, probar,request.POST['server'])
    task.start()
    return redirect("/devices")

def programar(request):
    idserver = request.POST['server']
    idhora = request.POST['hora']
    agregarSchedule(request, idserver, idhora)
    hoy = datetime.now()
    agenda = Schedule.objects.get(hora=idhora)
    agenda = agenda.hora.split(':')
    print(agenda)
    now = datetime.now()
    run = datetime(now.year, now.month, now.day ,int(agenda[0]),int(agenda[1]))
    delay = (run - now).total_seconds()
    print(delay)
    multiThread(request,delay)
    agenda=0

    return redirect("/devices")

def cerrar(request):
    del request.session['usuario']
    del request.session['id']
    return redirect("/")

def menu(request):
    return render(request, "menu.html")
