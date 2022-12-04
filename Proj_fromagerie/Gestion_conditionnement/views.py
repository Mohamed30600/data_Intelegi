from django.shortcuts import render,redirect

from Gestion_conditionnement.models import TConditionnement
from Gestion_conditionnement.forms import Conditionnementform


def listConditionnement(request):
    conditionnement = TConditionnement.objects.all()
    return render (request,"listConditionnement.html",{'tconditionnement':conditionnement})

def addconditionnement(request):
        if request.method == "POST":
            form = Conditionnementform(request.POST)
            if form.is_valid():
                try:
                    form.save()
                    return redirect('/objets')
                except:
                    pass
            
        else:
               form = Conditionnementform()
        return render (request,'addConditionnement.html',{'form':form})