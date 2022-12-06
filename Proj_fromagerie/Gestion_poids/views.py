from django.shortcuts import render, redirect
from Gestion_poids.models import TPoids
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

def readtable(request):
    timbre = TPoids.objects.all()
    return render(request,"first.html",{'t_poids':timbre})

def add(request):
  template = loader.get_template('add.html')
  print('toto')
  return HttpResponse(template.render({}, request))

def addrecord(request):
  x = request.POST['vmin']
  y = request.POST['vtimbre']
  newshit = TPoids(valmin=x, valtimbre=y)
  newshit.save()
  return HttpResponseRedirect(reverse('readtable'))

def delete(request,pvalmin):
  TPoids.objects.filter(valmin=pvalmin).delete() 
  return HttpResponseRedirect(reverse('readtable'))

# Create your views here.
