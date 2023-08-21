from rest_framework import serializers 
from .models import Piece


class PieceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piece
        fields = ['id','nom','prix','qts','piece_image']