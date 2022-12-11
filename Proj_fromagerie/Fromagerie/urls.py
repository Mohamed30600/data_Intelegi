"""Fromagerie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
import Authentification.views
import Gestion_utilisateurs.views
import Gestion_communes.views
import Gestion_objets.views
import Gestion_conditionnement.views
#vue generique de connexion fournit par django
from django.contrib.auth.views import LoginView
from django.urls import path, include

urlpatterns = [
    path('Gestion_poids/', include('Gestion_poids.urls')),
    path('admin/', admin.site.urls),
     
   path('login/', Authentification.views.login_page, name='login'),
   path('signup/',Authentification.views.signup_page,name = 'signup'),
   path('',Authentification.views.home,name='home'),
   path('utilisateurs/',Gestion_utilisateurs.views.ListeUtilisateurs,name='listeUtilisateurs'),
   path('delUtilisateur/<pk>',Gestion_utilisateurs.views.delUtilisateur,name='delUtilisateur'),
   path('communes/',Gestion_communes.views.listeCommune,name='listeCommunes'),
   path('addCommune/',Gestion_communes.views.addCommune,name='addCommune'),
   path('updateCommune/<pk>',Gestion_communes.views.updateCommune,name='updateCommune'),
   path('delCommune/<pk>',Gestion_communes.views.delCommune,name='delCommune'),
   path('objets/',Gestion_objets.views.listObjets,name='liste_objets'),
   path('addObjet/',Gestion_objets.views.addObjet,name='addObjet'),
   path('updateObjet/<pk>',Gestion_objets.views.updateObjet,name='updateObjet'),
    path('delObjet/<pk>',Gestion_objets.views.delObjet,name='delObjet'),
    path('conditionnement/',Gestion_conditionnement.views.listConditionnement,name='conditionnement'),
    path('addconditionnement/',Gestion_conditionnement.views.addconditionnement,name='addconditionnement'),
    path('updateConditionement/<pk>',Gestion_conditionnement.views.updateConditionnement,name='updateConditionement'),
    path('delconditionnement/<pk>',Gestion_conditionnement.views.delConditionement,name='delConditionement'),
   
]
