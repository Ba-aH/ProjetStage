from django.db import models
from utilisateur.models import User
from piece.models import Piece
# Create your models here.

class Panier (models.Model):
    utilisateur = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

class Panierpieces(models.Model):
    piece = models.ForeignKey(Piece,on_delete=models.CASCADE)
    qts = models.PositiveIntegerField(default=1)

