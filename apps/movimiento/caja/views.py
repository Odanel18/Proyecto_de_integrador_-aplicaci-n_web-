from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics

from .models import Caja
from .serializers import CajaSerializer
from drf_yasg.utils import swagger_auto_schema

class CajaApiView(APIView):
    def get(self, request):
     Serializer= CajaSerializer(Caja.objects.using('default').filter(estado=True), many=True)
     return Response(status=status.HTTP_200_OK, data=Serializer.data)
    
    @swagger_auto_schema(request_body=CajaSerializer, responses={201: CajaSerializer})
    def post(self, resquest):
       serializer=CajaSerializer(data= resquest.data)
       serializer.is_valid(raise_exception=True)
       serializer.save()
       return Response(data=serializer.data)
    
class CajaIDAPIView(APIView):   
    @swagger_auto_schema(request_body=CajaSerializer, responses={200: CajaSerializer})
    def patch(self, request, pk):
        
        try:
            caja = Caja.objects.filter(estado=True).get(pk=pk)
        except Caja.DoesNotExist:
            return Response({'error': 'Caja no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CajaSerializer(caja, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
      
        try:
            caja = Caja.objects.filter(estado=True).get(pk=pk)
        except Caja.DoesNotExist:
            return Response({'error': 'Caja no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        caja.estado=False # Eliminado logico
        caja.save()
        return Response(status=status.HTTP_204_NO_CONTENT) 