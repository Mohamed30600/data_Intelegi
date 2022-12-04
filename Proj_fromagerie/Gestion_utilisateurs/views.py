from django.shortcuts import render
from fastapi import FastAPI
import pickle
from Authentification.models import TUtilisateur

app =FastAPI()

def ListeUtilisateurs(request):
    liste=TUtilisateur.objects.values_list("code_utilisateur","first_name","role",named=True)
    print(liste)
    return render (request,'Gestion_utilisateurs/listeUtilisateurs.html',{'liste':liste})

