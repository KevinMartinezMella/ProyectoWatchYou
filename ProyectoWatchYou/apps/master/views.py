from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from apps.usuarios.models import Usuario
from apps.servidores.views import crear,read,update,delete
from apps.clases.monitor import Monitor, Validar
from apps.schedules.models import *
from apps.schedules.views import agregarSchedule
from datetime import datetime, timezone
import schedules
import time


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
        servers = read(request)
        context = {
            "usuario_actual": user_actual,
            "servers":servers,
        }
        return render(request, 'dashboard.html', context)
    else:
        return redirect("/")

def devices(request):
    if request.method == "GET" and "usuario" in request.session:
        usuario_actual = request.session["nombre"]
        user_actual = usuario_actual.upper()
        servers = read(request)
        context = {
            "usuario_actual": user_actual,
            "servers":servers,
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

def programar(request):
    idserver = request.POST['select']
    idhora = request.POST['hora']
    agregarSchedule(request, idserver, idhora)
    hoy = datetime.now()
    agenda = Schedule.objects.get(id = idserver)
    time = "%2d:%02d" %(hoy.hour, hoy.minute)
    print(idhora)
    schedules.every().day.at("idhora").do(probar(request))
    while True:
        try:
            schedules.run_pending()
            time.sleep(1)
        except:
            continue
        stop = input('Presiona q para finalizar el programa')
        if stop=='q':
            break
    # print("%2d:%02d" %(hoy.hour, hoy.minute))
        # probar(idserver = idserver)

    # return redirect("/devices")

def probar(request):
    # idserver = request.POST['select']
    idserver = "1"
    monitor = Monitor()
    isUp = monitor.ping(idserver)
    validar = Validar()
    validar.verificar(isUp)
    return redirect("/devices")

def cerrar(request):
    del request.session['usuario']
    del request.session['id']
    return redirect("/")

# def probandoPrueba(request):
#     probar()
#     return HttpResponse("funciona")


# schedule.every().day.at("14:44").do(cerrar(request))

# while True:
#     schedule.run_pending()
#     time.sleep(1)