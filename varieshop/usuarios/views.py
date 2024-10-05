from django.shortcuts import render
from .forms import RegistrarUsuarios

# Create your views here.
def usuarios(request):
    forms = RegistrarUsuarios()
    return render(request,"",{"forms":forms})