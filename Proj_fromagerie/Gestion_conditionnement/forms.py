from django import forms
from Gestion_conditionnement.models import TConditionnement


class Conditionnementform(forms.ModelForm):
    class Meta:
        model = TConditionnement
        fields = ['libcondit','poidscondit','prixcond']
        widgets = {
                   'libcondit': forms.TextInput(attrs={'class':'form-control'}),
                   'poidscondit': forms.TextInput(attrs={'class':'form-control'}),
                   'prixcond': forms.TextInput(attrs={'class':'form-control'}),
                   }