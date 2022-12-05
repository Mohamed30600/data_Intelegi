from django.shortcuts import render,redirect
from fastapi import FastAPI
import pickle
from Authentification.models import TUtilisateur

app =FastAPI()

def ListeUtilisateurs(request):
    liste=TUtilisateur.objects.values_list("code_utilisateur","username","first_name","role",named=True)
    print(liste)
    return render (request,'Gestion_utilisateurs/listeUtilisateurs.html',{'liste':liste})

def delUtilisateur(request,pk):
    utilisateur =TUtilisateur.objects.get(code_utilisateur=pk)
    utilisateur.delete()
    return redirect("/utilisateurs")