Primeros pasos:

1) Instrucción crear Entorno virtual: virtualenv <nombre entorno>
2) Instrucción entrar Entorno virtual: source appenv/bin/activate
3) Instrucción desactivar Entorno virtual: deactivate 
4) Instrucción eliminar Entorno virtual: rm -rf <nombre entorno>
5) Crear el proyecto: django-admin starproject <nombre proyecto>
6) Crear aplicación: django-admin startapp <nombre app>
7) Instrucción para ejecutar el proyecto: python manage.py runserver
8) Instrucción crear archivo requirements.txt: pip freeze > requirements.txt
9) Instrucciones para migrar la base de datos:
    python manage.py makemigrations 
    python manage.py migrate

10) Instrucción crear un superusuario: python manage.py createsuperuser
# Fin

