from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Compras,DetalleCompra
from .serializers import CompraSerializer,DetalleCompraSerializer
from drf_yasg.utils import swagger_auto_schema

class CompraAPIView (APIView):
    @swagger_auto_schema(responses={200: CompraSerializer(many=True)})
    def get(self,request):
        Serializer= CompraSerializer(Compras.objects.using('default').filter(estado=True), many=True)
        return Response(status=status.HTTP_200_OK, data=Serializer.data)
    
    @swagger_auto_schema(request_body=CompraSerializer, responses={201: CompraSerializer})
    def post(self, resquest):
       serializer=DetalleCompraSerializer(data= resquest.data)
       serializer.is_valid(raise_exception=True)
       serializer.save()
       return Response(status=status.HTTP_201_CREATED, data=serializer.data)

class CompraIDAPIView(APIView):   
    @swagger_auto_schema(request_body=CompraSerializer, responses={200: CompraSerializer})
    def patch(self, request, pk):
        
        try:
            compra = Compras.objects.filter(estado=True).get(pk=pk)
        except Compras.DoesNotExist:
            return Response({'error': 'Compra no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CompraSerializer(compra, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
      
        try:
            compra = Compras.objects.filter(estado=True).get(pk=pk)
        except Compras.DoesNotExist:
            return Response({'error': 'Compra no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        compra.estado=False # Eliminado logico
        compra.save()
        return Response(status=status.HTTP_204_NO_CONTENT) 


class DetallecompraAPIView (APIView):
    def get(self,request):
        Serializer= DetalleCompraSerializer(DetalleCompra.objects.filter(estado=True), many= True)
        return Response(status=status.HTTP_200_OK,data= Serializer.data)
    
    @swagger_auto_schema(request_body=DetalleCompraSerializer, responses= {201: DetalleCompraSerializer})
    def post(self, resquest):
       serializer=DetalleCompraSerializer(data= resquest.data)
       serializer.is_valid(raise_exception=True)
       serializer.save()
       return Response(status=status.HTTP_201_CREATED, data=serializer.data)


class DetallecompraIDAPIView(APIView):   
    @swagger_auto_schema(request_body=DetalleCompraSerializer, responses={200: DetalleCompraSerializer})
    def patch(self, request, pk):
        
        try:
            detalle = DetalleCompra.objects.filter(estado=True).get(pk=pk)
        except DetalleCompra.DoesNotExist:
            return Response({'error': 'Detalle compra no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = DetalleCompraSerializer(detalle, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
      
        try:
            detalle = DetalleCompra.objects.filter(estado=True).get(pk=pk)
        except DetalleCompra.DoesNotExist:
            return Response({'error': 'Detalle compra no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        detalle.estado=False # Eliminado logico
        detalle.save()
        return Response(status=status.HTTP_204_NO_CONTENT) 