from django.shortcuts import render
from apps.usuarios.models import Usuario

# Create your views here.

def index(request):
    if request.method == "GET":
        return render(request,'index.html')
    elif request.method == "POST":
        pass

def dashboard(request):
    return render(request, 'dashboard.html')

def devices(request):
    return render(request,'devices.html')