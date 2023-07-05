from django.shortcuts import render
from .models import region, comuna
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import EmailForm

# Create your views here.
def email_view(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        user_email = request.POST.get('user_email')
        user_message = request.POST.get('user_message')

        subject = 'Nuevo correo de un usuario'
        email_message = f"Nombre del usuario: {user_name}\nCorreo del usuario: {user_email}\nMensaje: {user_message}"
        from_email = 'tomasgarrido0212@gmail.com'
        recipient_list = ['tomasgarrido0212@gmail.com']

        send_mail(subject, email_message, from_email, recipient_list)

        # Puedes redirigir a otra página o mostrar un mensaje de éxito aquí
        return render(request, 'contacto.html')

    return render(request, 'contacto.html')



def index(request):
    return render(request, "index.html")

def home(request):
    return render(request, "home.html")

def createuser(request):
    if request.method != "POST":
        regiones = region.objects.all()
        comunas = comuna.objects.all()
        context = {"regions" : regiones, "comun" : comunas}
        return render(request, "create-account.html", context)
    else:
        rut = request.POST["rut"]
    return render(request, "create-account.html", context)


def login(request):    
    return render(request, "login.html")

def producto(request):
    return render(request, 'producto.html')

def contacto(request):
    return render(request, "contacto.html")

def nosotros(request):
    return render(request, "nosotros.html")
