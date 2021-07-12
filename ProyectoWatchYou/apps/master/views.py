from django.shortcuts import redirect, render
from apps.usuarios.models import Usuario

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
        context = {
            "usuario_actual": user_actual
        }
        return render(request, 'dashboard.html', context)
    else:
        return redirect("/")

def devices(request):
    if request.method == "GET" and "usuario" in request.session:
        return render(request,'devices.html')
    else:
        return redirect("/")

def cerrar(request):
    del request.session['usuario']
    del request.session['id']
    return redirect("/")