from django.shortcuts import redirect, render
from . models import *

# Create your views here.
def index(request):
    return render (request,'index.html')