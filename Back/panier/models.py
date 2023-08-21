from django.db import models
from utilisateur.models import User
from piece.models import Piece
# Create your models here.

class Panier (models.Model):
    utilisateur = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Panier for {self.utilisateur.username}"


class Panierpiece(models.Model):
    panier = models.ForeignKey(Panier, on_delete=models.CASCADE)
    piece = models.ForeignKey(Piece,on_delete=models.CASCADE)
    qts = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.qts}x {self.piece.nom} in {self.panier}"

    def total_price(self):
        return self.qts * self.piece.prix  