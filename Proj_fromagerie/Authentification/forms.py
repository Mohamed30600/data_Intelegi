from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import get_user_model

class SingupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()  #permet d obtenir le model user de django
        fields= ('username','email','first_name','last_name','role')
        
        



class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label='Nom d’utilisateur')
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')