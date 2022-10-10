from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required #Se usa este decorador para impedir que el usuario acceda a las funciones que no queremos que haya acceso y pueda hacerlo únicamente si hace log in.
#importar login requerido
from myApp.form import CustomUserCreationForm
#importar el formulario
from django.urls import reverse
#importar login
from django.contrib.auth import login



# Añadir que la autentificación es obligatoria para acceder
@login_required  #Se usa este decorador para impedir que el usuario acceda a las funciones que no queremos que haya acceso y pueda hacerlo únicamente si hace log in.
def home(request):
    return render(request,
                  'home.html',
                  context={'sepal_length': 5.1, 'sepal_width': 3.5,
                           'petal_length': 1.4, 'petal_width': 0.2,
                           'class': "Iris Setosa"})


def register(request):
    if request.method == "GET":
        #  pasar el formulario a la plantilla de registro
        return render(request, "registration/register.html",
                        {"form": CustomUserCreationForm})
    elif request.method == "POST":
        # Guardar el usuario siguiendo el formulario
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("home"))
