from django.shortcuts import render,redirect

from Gestion_objets.models import TObjet
from  Gestion_conditionnement.models import TConditionnement
from Gestion_objets.forms import Objetform


def listObjets (request):
    objets = TObjet.objects.all()
    
    return render (request,"listObjet.html",{'tobjet':objets})
    

def addObjet(request):
        if request.method == "POST":
            form = Objetform(request.POST)
            if form.is_valid():
                try:
                    form.save()
                    return redirect('/objets')
                except:
                    pass
            
        else:
               form = Objetform()
        return render (request,'addObjet.html',{'form':form})


def updateObjet (request,pk):
            objet = TObjet.objects.get(codobj=pk)
            if request.method == 'POST':
                form = Objetform(request.POST,instance=objet)
                if form.is_valid():
                    form.save()
                    return redirect ("/objets")
            return render(request,'updateObjet.html',{'t_objet':objet})
        
        

def delObjet(request,pk):
    commune =TObjet.objects.get(codobj=pk)
    commune.delete()
    return redirect("/objets")
