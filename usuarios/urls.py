from django.urls import path

from . import views

urlpatterns = [
    # Ruta principal para el formulario de validación
    path("", views.registro_usuario, name="registro_usuario"),
    path("registro/", views.registro_usuario, name="registro_usuario_alt"),
]
