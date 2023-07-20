from rest_framework import serializers
from piece.models import Piece


class ItemSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Piece
        fields = '__all__'
