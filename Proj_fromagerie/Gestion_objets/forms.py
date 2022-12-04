from django import forms
from Gestion_communes.models import TCommunes
from Gestion_objets.models import TObjet


class Objetform(forms.ModelForm):
    class Meta:
        model = TObjet
        fields = ['libobj','tailleobj','puobj','poidsobj','o_imp','points']
        widgets = {
                   'libobj': forms.TextInput(attrs={'class':'form-control'}),
                   'tailleobj': forms.TextInput(attrs={'class':'form-control'}),
                   'puobj': forms.TextInput(attrs={'class':'form-control'}),
                   'poidsobj': forms.TextInput(attrs={'class':'form-control'}),
                   'o_imp': forms.TextInput(attrs={'class':'form-control'}),
                   'points': forms.TextInput(attrs={'class':'form-control'}),
                   }