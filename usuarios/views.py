from django.contrib import messages
from django.shortcuts import render

from .forms import RegistroUsuarioForm


def registro_usuario(request):
    """
    Vista para manejar el registro de usuarios y demostrar la
    buena práctica de Validación de Datos de Entrada.
    """
    if request.method == "POST":
        # Se instancia el formulario con los datos enviados por el usuario
        form = RegistroUsuarioForm(request.POST)

        # Aquí ocurre la magia de la validación.
        # form.is_valid() ejecuta todas las validaciones definidas en forms.py
        if form.is_valid():
            # Si los datos son válidos, podemos acceder a ellos de forma segura
            nombre = form.cleaned_data["nombre"]
            email = form.cleaned_data["email"]

            # Simulamos el guardado en base de datos u otra acción.
            # En un caso real, guardaríamos el modelo aquí.

            messages.success(
                request,
                f"¡Registro exitoso! Bienvenido, {nombre} (registrado con el correo {email}). Los datos han sido validados correctamente.",
            )

            # Limpiamos el formulario para un nuevo registro
            form = RegistroUsuarioForm()
        else:
            # Si form.is_valid() retorna False, los errores ya están vinculados al formulario
            # y se mostrarán automáticamente en la plantilla.
            messages.error(
                request,
                "Ocurrió un error al procesar tu solicitud. Por favor, revisa y corrige los campos remarcados.",
            )
    else:
        # Petición GET, se muestra el formulario vacío
        form = RegistroUsuarioForm()

    context = {
        "form": form,
    }

    return render(request, "usuarios/registro.html", context)
