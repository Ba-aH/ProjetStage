from rest_framework import serializers
from .models import Panier, Panierpiece

class PanierpieceSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()
    
    class Meta:
        model = Panierpiece
        fields = ('id', 'panier', 'piece', 'qts', 'total_price')

    def get_total_price(self, obj):
        return obj.total_price()

class PanierSerializer(serializers.ModelSerializer):
    panierpieces = PanierpieceSerializer(many=True, read_only=True)

    class Meta:
        model = Panier
        fields = ('id', 'utilisateur', 'date', 'panierpieces')
