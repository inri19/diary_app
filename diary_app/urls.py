from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('diary/accueil/', accueil, name='accueil'),
    path('diary/nouveau/', nouveau_journal, name='nouveau_journal'),
    path('diary/journal_details/<int:id>/', journal_details, name='journal_details'),
    path('diary/modifier/<int:id>/', modifier_journal, name='modifier_journal'),
    path('diary/supprimer/<int:id>/', supprimer_journal, name='supprimer_journal'),
]