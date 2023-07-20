from django.db import models
from utilisateur.models import User
from piece.models import Piece

# Create your models here.
class Commande (models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    Piece = models.ForeignKey(Piece, on_delete=models.CASCADE)
    date_commande = models.DateTimeField(auto_now_add=True)
    qts = models.PositiveIntegerField(default=1)
