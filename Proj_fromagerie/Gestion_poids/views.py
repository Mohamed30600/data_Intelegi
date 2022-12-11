from django.shortcuts import render, redirect
from Gestion_poids.models import TPoids
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse


# vue responsable de l'affichage du tableau
def affiche_table(request):
    timbre = TPoids.objects.all()    
    return render(request,"page_accueil.html",{'t_poids':timbre})

# vue responsable de l'affichage du formulaire d'ajout d'un objet dans la table poids
def ajout(request):
  return render(request, 'ajout.html')

# vue responsable de l'ajout d'un objet dans la table et redirection sur la page d'accueil
def ajout_saisi_donnees(request):
  x = request.POST['vmin']
  y = request.POST['vtimbre']
  nouvelle_instance = TPoids(valmin=x, valtimbre=y)
  nouvelle_instance.save()
  return redirect('/Gestion_poids')

# vue responsable de la suppression d'une instance 
def delete(request,pvalmin):
  TPoids.objects.filter(valmin=pvalmin).delete() 
  return redirect('/Gestion_poids')

# vue responsable de l'affichage du formulaire de modification d'un objet dans la table poids
def modif(request,pvalmin):
  poids = TPoids.objects.filter(valmin=pvalmin)
  return render(request, "update.html",{'opoids': poids[0]})

# vue responsable de l'ajout d'un objet dans la table et redirection sur la page d'accueil
def update_record(request):
  vmin = request.POST['vmin']
  vtimbre = request.POST['vtimbre']
  poids = TPoids.objects.filter(valmin=vmin)
  poids = poids[0]
  poids.valtimbre=vtimbre
  poids.save()
  return redirect('/Gestion_poids')