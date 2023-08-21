from django.shortcuts import render
from django.http import JsonResponse
from .models import Piece
from .serializers import PieceSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET','POST'])
def piece_list(request,format=None):
    if request.method == 'GET':
        pieces = Piece.objects.all()
        print(pieces[0].piece_image)
        serializer = PieceSerializer(pieces,many=True)
        return Response(serializer.data)
     
    if request.method == 'POST':
        serializer = PieceSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)



@api_view(['GET','PUT','DELETE'])
def piece_detail(request, id, format=None):

    try :
        piece = Piece.objects.get(pk=id)
    except Piece.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PieceSerializer(piece)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = PieceSerializer(piece,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        piece.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)