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
                    return redirect('/conditionnement')
                except:
                    pass
            
        else:
               form = Conditionnementform()
        return render (request,'addconditionnement.html',{'form':form})
    
def updateConditionnement (request,pk):
            conditionnement = TConditionnement.objects.get(idcondit=pk)
            if request.method == 'POST':
                form = Conditionnementform(request.POST,instance=conditionnement)
                if form.is_valid():
                    form.save()
                    return redirect ("/conditionnement")
            return render(request,'updateConditionement.html',{'tconditionvement':conditionnement})
        
        
def delConditionement (request,pk):
    conditionnement =TConditionnement.objects.get(idcondit=pk)
    conditionnement.delete()
    return redirect("/conditionnement")