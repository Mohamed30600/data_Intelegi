
from django import forms
from Gestion_communes.models import TCommunes


class CommuneForm(forms.ModelForm):
    class Meta:
        model = TCommunes
        fields = ['communes','dep','cp']
        widgets = {'communes': forms.TextInput(attrs={'class':'form-control'}),
                   'dep': forms.TextInput(attrs={'class':'form-control'}),
                   'cp': forms.TextInput(attrs={'class':'form-control'}),
                   }