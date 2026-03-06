# Buenas Prácticas PentaCode - Proyecto de Ejemplo

Este repositorio forma parte de la actividad de implementación de buenas prácticas de desarrollo de software asignada por el docente. 

## Información del Equipo (Ejemplo)
- **Integrante que comparte el repositorio:** *Anotar tu nombre o el de tu equipo aquí*

## 1. Buena Práctica Implementada

**Validación de Datos de Entrada**

La validación de datos de entrada (Input Validation) es un pilar fundamental tanto de la seguridad como de la usabilidad de las aplicaciones web. Consiste en garantizar que la información suministrada al sistema por el usuario o por sistemas externos cumpla con los formatos, tipos e intervalos esperados antes de ser procesada y almacenada.

En este repositorio implementamos esta práctica utilizando **Django Forms**.

**¿Por qué es importante?**
- Previene vulnerabilidades de seguridad como inyecciones (SQLi, XSS, etc.).
- Asegura la integridad de los datos en la base de datos (por ejemplo, que una edad nunca sea negativa).
- Mejora la experiencia del usuario devolviendo mensajes claros y oportunos en caso de ingreso de datos incorrectos.

**¿Cómo se implementó en el proyecto?**
El ejemplo se encuentra en la aplicación `usuarios`. Creamos el formulario `RegistroUsuarioForm` (`usuarios/forms.py`):
1. **Validación de tipos y rangos:** Obligamos a que la edad esté entre 18 y 120 años y verificamos la longitud mínima de las contraseñas.
2. **Expresiones Regulares (RegEx):** Implementamos un método `clean_nombre` para garantizar que el campo "nombre" solo contenga caracteres alfabéticos, rechazando números y caracteres especiales.
3. **Validación de negocio:** En `clean_email`, garantizamos que no se introduzcan cuentas de correos consideradas basura temporal (ej: `@test.com`, `@tempmail.com`).
4. **Validación cruzada de campos:** Sobreescribimos el método `clean()` completo para cotejar que la "contraseña" y "confirmar contraseña" sean exactamente iguales. Todo ello sin depender del modelo de base de datos directamente, asegurando los datos en la primera capa.

Dichas validaciones impiden llegar a la vista (`views.py`) si los datos son incorrectos y devuelven un feedback amigable para el usuario a través de la plantilla `registro.html`.

## 2. Librerías y Herramientas Utilizadas

- **Django**: (Librería principal, core del framework de Python). Se usa particularmente `django.forms` para la validación centralizada.
- **re (Regular Expressions)**: Módulo nativo de Python que utilizamos en `forms.py` para asegurar que el contenido alfabético con `re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$")`.
- **Bootstrap 5 (vía CDN)**: Librería de estilos CSS para realizar una interfaz clara donde se puedan exponer visualmente los errores capturados.

## 3. Enlace del Repositorio PÚBLICO

*Anotar aquí el enlace al repositorio de GitHub correspondiente.*

---

## Instrucciones para la Ejecución del Proyecto

Sigue estos pasos para clonar el proyecto, inicializar su ambiente localmente y verificar su funcionamiento.

1. **Clona este repositorio o descarga el código fuente:**

   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd BuenasPracticasPentaCode
   ```

2. **Crea y activa el entorno virtual:**

   *Windows:*
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```
   *Mac / Linux:*
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instala las dependencias necesarias** (Asegúrate de tener un archivo req o instala Django local):

   ```bash
   pip install django
   ```

4. **Ejecuta las migraciones de base de datos** (necesarias para las sesiones integradas en Django):

   ```bash
   python manage.py migrate
   ```

5. **Levanta el servidor local:**

   ```bash
   python manage.py runserver
   ```

6. **Probando la Validación de Datos:**

   Abre un navegador e ingresa a la siguiente dirección: 
   [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

   - Intenta hacer lo siguiente para probar las validaciones de error:
     - Enviar el formulario vacío.
     - Escribir números en el nombre (`Juan123`).
     - Utilizar un correo restringido (ej: `prueba@test.com`).
     - Escribir una edad menor de 18 años.
     - Introducir dos contraseñas distintas.
   - Finalmente, rellena los datos correctamente y verifica el mensaje de éxito del registro.
