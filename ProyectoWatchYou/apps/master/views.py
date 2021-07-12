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
            return redirect("/dashboard")
        else:
            return redirect("/")

def dashboard(request):
    return render(request, 'dashboard.html')

def devices(request):
    return render(request,'devices.html')