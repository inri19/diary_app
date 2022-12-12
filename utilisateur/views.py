from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def inscription(request):

    if request.method == 'POST' :

        form = UserCreationForm(request.POST)

        if form.is_valid() :

            form.save()

            messages.success(request, 'Inscription Reussi')

        else :

            messages.info(request, 'Les mot de passes ne sont pas identiques')
    else :

        form = UserCreationForm()

    dico = { "form" : form }

    return render(request, 'utilisateur/inscription.html', dico)