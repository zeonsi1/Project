from django.shortcuts import render
from .models import region, comuna
# Create your views here.

def index(request):
    return render(request, "index.html")

def home(request):
    return render(request, "home.html")

def createuser(request):
    return render(request, "create-account.html")

def login(request):    
    return render(request, "login.html")

def producto(request):
    return render(request, 'producto.html')

def contacto(request):
    return render(request, "contacto.html")

def nosotros(request):
    return render(request, "nosotros.html")

def signup(request):
    if request.method != "POST":
        regiones = region.objects.all()
        comunas = comuna.objects.all()
        context = {"regions" : regiones, "comun" : comunas}
        return render(request, "create-account.html", context)
    else:
        rut = request.POST["rut"]
    return render(request, "create-account.html", context)