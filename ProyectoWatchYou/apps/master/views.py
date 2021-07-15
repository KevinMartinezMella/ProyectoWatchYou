from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from apps.usuarios.models import Usuario
from apps.servidores.views import crear,read,update,delete
from apps.clases.monitor import Monitor, Validar


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
    context = {
        "id":request.POST['id'],
        "hora":request.POST['hora']
    }

    return redirect("/devices")

def probar(request):
    idserver = request.POST['select']
    Monitor.ping(request,idserver)
    Validar.verificar(request)
    return HttpResponse(request)

def cerrar(request):
    del request.session['usuario']
    del request.session['id']
    return redirect("/")