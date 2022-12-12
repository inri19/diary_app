from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

# Create your views here.
def index(request):

    dico = {}

    return render(request, 'diary_app/index.html', dico)
    
def accueil(request):

    journals = Journal.objects.filter(utilisateur=request.user).order_by('-date_creation')

    dico = { "journals" : journals }

    return render(request, 'diary_app/accueil.html', dico)

def nouveau_journal(request):

    if request.method == 'POST' :

        titre = request.POST.get('titre')
        contenu = request.POST.get('contenu')

        if len(titre) == 0 or len(contenu) == 0 :

            messages.info(request, 'Tous les champs sont obligatoires')
        
        else :

            new_day = Journal(titre=titre, contenu=contenu, utilisateur=request.user)
            new_day.save()
            messages.success(request, 'Journal Enregistrer !')

            return redirect('/diary/accueil/')

    dico = {}

    return render(request, 'diary_app/nouveau_journal.html', dico)

def journal_details(request, id):

    journal = Journal.objects.get(id=id)

    dico = { "journal" : journal }

    return render(request, 'diary_app/journal_details.html', dico)

def modifier_journal(request, id):

    journal = Journal.objects.get(id=id)

    if request.method == 'POST' :

        titre = request.POST.get('titre')
        contenu = request.POST.get('contenu')

        if len(titre) == 0 or len(contenu) == 0 :

            messages.info(request, 'Tous les champs sont obligatoire')
        
        else :

            journal.titre = titre
            journal.contenu = contenu
            journal.save()

            messages.success(request, 'Journal Modifier')

            return redirect(f'/diary/journal_details/{id}')

    dico = { "journal" : journal }

    return render(request, 'diary_app/modifier_journal.html', dico)

def supprimer_journal(request, id):

    journal = Journal.objects.get(id=id)
    journal.delete()

    messages.success(request, 'Journal Supprimer !')

    return redirect('/diary/accueil')