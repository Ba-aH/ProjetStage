from rest_framework import serializers
from piece.models import Piece
from panier.models import Panier


class PieceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piece
        fields = '__all__'


class PanierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Panier
        fields = '__all__'