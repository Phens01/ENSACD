from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth import views as auth_views
from .models import *
from .forms import *

def home(request):
    return render(request, "home.html")


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Remplacez 'home' par le nom de votre vue d'accueil
        else:
            error_message = "Nom d'utilisateur ou mot de passe incorrect."
    else:
        error_message = None

    context = {
        'error_message': error_message,
    }
    return render(request, 'login.html', context)




def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Créez un nouvel utilisateur en utilisant les données du formulaire
            user = form.save()
            # Effectuez ici d'autres actions nécessaires, comme l'envoi d'un e-mail de confirmation, etc.
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def password_reset(request):
    return auth_views.PasswordResetView.as_view(
        template_name='password_reset.html',
        email_template_name='password_reset_email.html',
        subject_template_name='password_reset_subject.txt'
    )(request)