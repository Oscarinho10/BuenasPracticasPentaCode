"""
Formularios para la aplicación usuarios.
Aquí se implementa la buena práctica de "Validación de Datos de Entrada".
"""

import re

from django import forms


class RegistroUsuarioForm(forms.Form):
    # Definición de campos con validaciones básicas integradas
    nombre = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Ej. Juan Pérez"}
        ),
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "correo@ejemplo.com"}
        ),
        error_messages={
            "invalid": "Por favor, introduce una dirección de correo válida."
        },
    )
    edad = forms.IntegerField(
        required=True,
        min_value=18,
        max_value=120,
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Ej. 25"}
        ),
        error_messages={
            "min_value": "Debes ser mayor de 18 años para registrarte.",
            "max_value": "La edad ingresada no es válida.",
        },
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Contraseña"}
        ),
        required=True,
        min_length=8,
        error_messages={
            "min_length": "La contraseña debe tener al menos 8 caracteres."
        },
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Confirmar Contraseña"}
        ),
        required=True,
    )

    # 1. Validación de campo específico (clean_<nombre_campo>)
    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre")
        # Validar que el nombre solo contenga letras y espacios
        if not re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$", nombre):
            raise forms.ValidationError(
                "El nombre solo puede contener letras y espacios."
            )
        return nombre

    def clean_email(self):
        email = self.cleaned_data.get("email")
        # Validación de negocio adicional (ejemplo: rechazar correos temporales)
        dominios_prohibidos = ["test.com", "tempmail.com", "ejemplo.com"]
        dominio = email.split("@")[1]

        if dominio in dominios_prohibidos:
            raise forms.ValidationError(
                "No se permiten correos de dominios temporales o de prueba."
            )
        return email

    # 2. Validación cruzada entre múltiples campos (clean global)
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password:
            if password != confirm_password:
                # Opciones: Anexar error a un campo específico o de forma general
                self.add_error("confirm_password", "Las contraseñas no coinciden.")
                raise forms.ValidationError(
                    "Por favor, asegúrate de que ambas contraseñas coincidan."
                )

        return cleaned_data
