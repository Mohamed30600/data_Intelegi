from django.conf import settings
from django.contrib.auth import login
from django.shortcuts import redirect,render
from . import forms
from django.contrib.auth import login,logout, authenticate # import des fonctions login et authenticate

def home (request):
    return render(request,'authentification/home.html')

def signup_page(request):
    form = forms.SingupForm()
    if request.method == 'POST':
        form = forms.SingupForm(request.POST)
        if form.is_valid():
            user = form.save()
            #connexion de l utilisateur et redirection page home
            login(request,user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    
    return render(request,'authentification/signup.html',context={'form':form})



def logout_user(request):
        logout(request)
        return redirect('login')
    
    

def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = f'Bonjour, {user.username}! Vous êtes connecté.'
            else:
                message = 'Identifiants invalides.'
    return render(
        request, 'authentification/login.html', context={'form': form, 'message': message})
    
    
  