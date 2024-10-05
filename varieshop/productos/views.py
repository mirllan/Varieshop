from django.shortcuts import render
from .forms import RegistrarProducto
# Create your views here.

def productos(request):
    forms = RegistrarProducto()
    return render(request,"productos.html",{"forms":forms})
