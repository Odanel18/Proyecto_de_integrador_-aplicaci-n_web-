#from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Categorias
from .serializers import CategoriaSerializer
from drf_yasg.utils import swagger_auto_schema

class CategoriaApiView(APIView):
    @swagger_auto_schema(responses={200: CategoriaSerializer(many=True)})
    def get(self, request):
     Serializer= CategoriaSerializer(Categorias.objects.using('default').filter(estado=True), many=True)
     return Response(status=status.HTTP_200_OK, data=Serializer.data)

    @swagger_auto_schema(request_body=CategoriaSerializer, responses= {201: CategoriaSerializer})
    def post(self,request):
       serializer= CategoriaSerializer(data=request.data)
       serializer.is_valid(raise_exception=True)
       serializer.save()
       return Response(status=status.HTTP_201_CREATED,data=serializer.data)    
 
class CategoriaIDAPIView(APIView):   
    @swagger_auto_schema(request_body=CategoriaSerializer, responses={200: CategoriaSerializer})
    def patch(self, request, pk):
        
        try:
            categoria = Categorias.objects.get(pk=pk)
        except Categorias.DoesNotExist:
            return Response({'error': 'Categoria no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CategoriaSerializer(categoria, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
      
        try:
            categoria = Categorias.objects.get(pk=pk)
        except Categorias.DoesNotExist:
            return Response({'error': 'Categoria no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        categoria.estado=False # Eliminado logico
        categoria.save()
        # return Response(status=status.HTTP_204_NO_CONTENT) ¿