from rest_framework.response import Response
from rest_framework.decorators import api_view
from piece.models import Piece
from .serializers import PieceSerializer


@api_view(['GET'])
def getData(request):
    pieces = Piece.objects.all()
    serializer =PieceSerializer(pieces,many=True)
    return Response(serializer.data)