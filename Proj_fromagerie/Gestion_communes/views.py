from django.shortcuts import render,redirect
from Gestion_communes.models import TCommunes
from Gestion_communes.forms import CommuneForm

def listeCommune (request):
    listeC = TCommunes.objects.values_list('idcom','dep','cp','communes',named=True)
    return render (request,'listeCommunes.html',{'liste':listeC})


def addCommune (request):
        if request.method == "POST":
            form = CommuneForm(request.POST)
            if form.is_valid():
                try:
                    form.save()
                    return redirect('/communes')
                except:
                    pass
        else:
               form = CommuneForm()
        return render (request,'addCommune.html',{'form':form})


def updateCommune (request,pk):
            commune = TCommunes.objects.get(idcom=pk)
            if request.method == 'POST':
                form = CommuneForm(request.POST,instance=commune)
                if form.is_valid():
                    form.save()
                    return redirect ("/communes")
            return render(request,'updateCommune.html',{'commune':commune})
    # commune = TCommunes.objects.get(id=id)
    # print(commune)
    # return render (request,'updateCommune.html',{'commune':commune})
 
    

def delCommune(request,pk):
    commune =TCommunes.objects.get(idcom=pk)
    commune.delete()
    return redirect("/communes")
