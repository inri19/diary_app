from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Journal(models.Model):

    titre = models.CharField(max_length=50)
    contenu = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titre
