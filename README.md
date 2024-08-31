# Appkim

Appkim es una plataforma educativa desarrollada en Django donde estudiantes y profesores pueden inscribirse y gestionar cursos. 

## Descripción

Appkim permite a los usuarios registrarse como estudiantes o profesores y acceder a diversos cursos disponibles en la plataforma. Los estudiantes pueden inscribirse en los cursos, mientras que los profesores pueden gestionar sus clases y contenido.

## Características

- **Registro de usuarios**: Permite el registro de estudiantes y profesores.
- **Gestión de cursos**: Los profesores pueden crear y administrar cursos.
- **Inscripción en cursos**: Los estudiantes pueden inscribirse en los cursos disponibles.
- **Visualización de cursos**: Todos los usuarios pueden ver la lista de cursos disponibles.

## Tecnologías Utilizadas

- **Django**: Framework web utilizado para la creación de la aplicación.
- **SQL**: Base de datos para almacenar información sobre usuarios, cursos y registros.
- **HTML**: Plantillas utilizadas para la interfaz de usuario.

## Instalación

1. Clona este repositorio:
   ```bash
   https://github.com/yisel35/tercera_preentrega_KImberlyn-martinez..git
2 .Instala las dependencias:
   pip install -r requirements.txt
3. Realiza las migraciones de la base de datos:
   python manage.py migrate
4. Corre el servidor:
   python manage.py runserver
5. Accede a la aplicación en tu navegador:
   http://127.0.0.1:8000

## Funcionalidades y Ubicaciones

Inicio: Muestra una vista general de la plataforma. (/)

Crear Profesor: Formulario para agregar nuevos profesores. (/crear-profesor/)

Crear Estudiante: Formulario para agregar nuevos estudiantes. (/crear-estudiante/)

Crear Curso: Formulario para crear nuevos cursos. (/crear-curso/)

Buscar y Ver Resultados: Busca estudiantes, profesores o cursos y muestra los resultados. (/buscar/)

Visualizar Cursos Disponibles: Permite ver cursos si el usuario está habilitado. (/cursos/)

## Orden de Prueba de la Aplicación
Para probar Appkim, sigue los siguientes pasos:

**Página de Inicio:
Ruta: /
Descripción: Página de bienvenida con navegación a todas las secciones principales.

**Crear Profesor:
Ruta: /crear-profesor/
Vista: crear_profesor
Descripción: Muestra un formulario para crear un nuevo profesor y guardar la información en la base de datos.

**Crear Estudiante:
Ruta: /crear-estudiante/
Vista: crear_estudiante
Descripción: Muestra un formulario para crear un nuevo estudiante y guardar la información en la base de datos.

**Crear Curso:
Ruta: /crear-curso/
Vista: crear_curso
Descripción: Muestra un formulario para crear un nuevo curso y guardarlo en la base de datos.

**Buscar:
Ruta: /buscar/
Vista: buscar
Descripción: Permite buscar estudiantes, profesores y cursos mediante un término de búsqueda. La búsqueda valida si los usuarios están inscritos para mostrar los resultad

