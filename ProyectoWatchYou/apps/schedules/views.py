from apps.servidores.models import Servidor
from .models import *

from django.shortcuts import render

# Create your views here.

def agregarSchedule(request, idserver, idhora):
    server = Servidor.objects.get(id = idserver)
    schedule = Schedule(
        idserver = server,
        hora = idhora
    )
    schedule.save()


