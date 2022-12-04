from django.shortcuts import render

from Gestion_objets.models import TObjet


def listObjets (request):
    objets = TObjet.objects.all()
    print(objets)
    return render (request,"listObjet.html",{'tobjet':objets})
    
