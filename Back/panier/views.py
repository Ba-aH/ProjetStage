from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Panier, Panierpiece
from .serializers import PanierSerializer, PanierpieceSerializer 

@api_view(['GET', 'POST'])
def panier_list(request):
    if request.method == 'GET':
        paniers = Panier.objects.all()
        serializer = PanierSerializer(paniers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PanierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def panier_detail(request, pk):
    try:
        panier = Panier.objects.get(pk=pk)
    except Panier.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PanierSerializer(panier)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = PanierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        serializer = PanierSerializer(panier, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        panier.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

    
@api_view(['GET', 'POST'])
def panierpiece_list(request):
    if request.method == 'GET':
        panierpieces = Panierpiece.objects.all()
        serializer = PanierpieceSerializer(panierpieces, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PanierpieceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def panierpiece_detail(request, pk):
    try:
        panierpiece = Panierpiece.objects.get(pk=pk)
    except Panierpiece.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PanierpieceSerializer(panierpiece)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = PanierpieceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        serializer = PanierpieceSerializer(panierpiece, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        panierpiece.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)