First steps:

1) Create virtual enviroment: virtualenv <enviroment name>
2) Activate virtual enviroment: source appenv/bin/activate
3) To deactivate the virtual enviroment use: deactivate 
4) To delete the virtual enviroment use: rm -rf <enviroment name>
5) Create the project: django-admin starproject <project name>
6) Create app: django-admin startapp <app name>
7) Execute project: python manage.py runserver
8) To save packages in a file requirements.txt: pip freeze > requirements.txt
9) Instruction to migrate the database:
    python manage.py makemigrations 
    python manage.py migrate

10) Instruction to create a superuser: python manage.py createsuperuser
## End

