from django.urls import path, re_path, include
from myApp import views
from myApp.iris.views import irisData, insertData, updateData, deleteData

urlpatterns = [
    re_path(r'^home/', views.home, name='home'),
    # Añadir las urls para accounts
    path('accounts/', include('django.contrib.auth.urls')),
    #  Añadir las urls para register
    path('register/', views.register, name="register"),
    # Añadir las urls para iris. path('iris/' es el nombre de la url.
    path('iris/', irisData, name="iris"),
    # Añadir las urls para insertData
    path('insertData/', insertData, name="insertData"),
    # Añadir las urls para updateData
    path('updateData/', updateData, name="updateData"),
    # Añadir las urls para deleteData
    path('deleteData/', deleteData, name="deleteData"),
]
