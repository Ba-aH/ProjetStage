from django.db import models

# Create your models here.

class Piece(models.Model):
    nom = models.CharField(max_length=200)
    prix = models.DecimalField(max_digits=10,decimal_places=2)
    qts = models.PositiveIntegerField()
    piece_image = models.ImageField(null=True , blank=True,upload_to="images/")
