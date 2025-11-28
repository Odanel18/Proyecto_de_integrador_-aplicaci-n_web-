#from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics

from .models import Abonos
from .serializers import AbonoSerializer
from drf_yasg.utils import swagger_auto_schema


class AbonosApiView(APIView):
    def get(self, request):
     Serializer= AbonoSerializer(Abonos.objects.using('default').filter(estado=True), many=True)
     return Response(status=status.HTTP_200_OK, data=Serializer.data)
    
    @swagger_auto_schema(request_body=AbonoSerializer, responses={201: AbonoSerializer})
    def post(self,request):
        Serializer= AbonoSerializer(data=request.data)
        Serializer.is_valid(raise_exception=True)
        Serializer.save()
        return Response (status=status.HTTP_201_CREATED, data=Serializer.data)

class AbonosIDAPIView(APIView):   
    @swagger_auto_schema(request_body=AbonoSerializer, responses={200: AbonoSerializer})
    def patch(self, request, pk):
        
        try:
            abono = Abonos.objects.filter(estado=True).get(pk=pk)
        except Abonos.DoesNotExist:
            return Response({'error': 'Abono no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = AbonoSerializer(abono, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
      
        try:
            abono = Abonos.objects.filter(estado=True).get(pk=pk)
        except Abonos.DoesNotExist:
            return Response({'error': 'Abono no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        abono.estado=False # Eliminado logico
        abono.save()
        return Response(status=status.HTTP_204_NO_CONTENT) 
        