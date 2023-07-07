from django.shortcuts import render, redirect
from .models import producto, usuario, tipoUsuario
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import EmailForm
from django.contrib.auth import authenticate

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
        return render(request, "create-account.html")
    else:
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        appaterno = request.POST["apellidoPaterno"]
        apmaterno = request.POST["apellidoMaterno"]
        telefono = request.POST["telefono"]
        correo = request.POST["correo"]
        contrasena = request.POST["contrasena"]
        region = request.POST["region"]
        comuna = request.POST["comuna"]
        direccion = request.POST["direccion"]


        objTipo = tipoUsuario.objects.get(id_tipo = 1)
        objUsuario = usuario.objects.create(
            rut_usuario = rut,
            nombre = nombre,
            appaterno = appaterno,
            apmaterno = apmaterno,
            telefono = telefono,
            correo_usuario = correo,
            contra_usuario = contrasena,
            region_usuario = region,
            comuna_usuario = comuna,
            direccion_usuario = direccion,
            id_tipo = objTipo,
            activo = 1,
        )
        objUsuario.save()
        context = {"mensaje": "OK Registrado Correctamente"}
        return redirect('home')



def login(request):
    context = {}
    if request.method != 'POST':
        return render(request, "login.html")
    else:
        email = request.POST["correo"]
        password = request.POST["pass"]

        usuario = authenticate(request, correo_usuario = email, contra_usuario = password)
        if usuario is None:
            return render(request, "login.html", {
                'error': 'E-mail o contraseña es Incorrecto'
            })

def productos(request):
    products = producto.objects.all()
    context = {
        'product': products
    }
    return render(request, 'producto.html', context)

def contacto(request):
    return render(request, "contacto.html")

def nosotros(request):
    return render(request, "nosotros.html")
