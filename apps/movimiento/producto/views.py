from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Productos, DetalleProductos,Registro_Producto
from .serialezers import ProductoSerializer,DetalleProductoSerializer,Registro_ProductoSerialezer
from drf_yasg.utils import swagger_auto_schema

class ProductoAPIView (APIView):
    def get (self,request):
        serializer= ProductoSerializer(Productos.objects.filter(estado=True), many=True)
        return Response(data= serializer.data)
    
    @swagger_auto_schema(request_body=ProductoSerializer, responses= {201: ProductoSerializer})
    def post (self,request):
        serializer= ProductoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)

class ProductoIDAPIView(APIView):   
    @swagger_auto_schema(request_body=ProductoSerializer, responses={200: ProductoSerializer})
    def patch(self, request, pk):
        
        try:
            producto = Productos.objects.filter(estado=True).get(pk=pk)
        except Productos.DoesNotExist:
            return Response({'error': 'Producto no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductoSerializer(producto, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
      
        try:
            producto = Productos.objects.filter(estado=True).get(pk=pk)
        except Productos.DoesNotExist:
            return Response({'error': 'Producto no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        producto.estado=False # Eliminado logico
        producto.save()
        return Response(status=status.HTTP_204_NO_CONTENT)     


class DetalleProductoAPIVew (APIView):
    def get (self,request):
        serializer= DetalleProductoSerializer(DetalleProductos.objects.filter(estado=True), many=True)
        return Response(data= serializer.data)
    
    @swagger_auto_schema(request_body=DetalleProductoSerializer, responses= {201: DetalleProductoSerializer})
    def post (self,request):
        serializer= DetalleProductoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)

class DetalleProductosIDAPIView(APIView):   
    @swagger_auto_schema(request_body=DetalleProductoSerializer, responses={200: DetalleProductoSerializer})
    def patch(self, request, pk):
        
        try:
            detalle = DetalleProductos.objects.filter(estado=True).get(pk=pk)
        except DetalleProductos.DoesNotExist:
            return Response({'error': 'Detale producto no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = DetalleProductoSerializer(detalle, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
      
        try:
            detalle = DetalleProductoSerializer.objects.filter(estado=True).get(pk=pk)
        except DetalleProductos.DoesNotExist:
            return Response({'error': 'Detalle producto no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        detalle.estado=False # Eliminado logico
        detalle.save()
        return Response(status=status.HTTP_204_NO_CONTENT) 



class Registro_ProductoApiView(APIView):
    def get(self, request):
     Serializer= Registro_ProductoSerialezer(Registro_Producto.objects.using('default').filter(estado=True), many=True)
     return Response(status=status.HTTP_200_OK, data=Serializer.data)
    
    @swagger_auto_schema(request_body=Registro_ProductoSerialezer, responses={201: Registro_ProductoSerialezer})
    def post(self,request):
        Serializer= Registro_ProductoSerialezer(data=request.data)
        Serializer.is_valid(raise_exception=True)
        Serializer.save()
        return Response (status=status.HTTP_201_CREATED, data=Serializer.data)

class Registro_ProductoIDAPIView(APIView):   
    @swagger_auto_schema(request_body=Registro_ProductoSerialezer, responses={200: Registro_ProductoSerialezer})
    def patch(self, request, pk):
        
        try:
            inventarioLote = Registro_Producto.objects.filter(estado=True).get(pk=pk)
        except Registro_Producto.DoesNotExist:
            return Response({'error': 'Lote no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = Registro_ProductoSerialezer(inventarioLote, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
      
        try:
            inventarioLote = Registro_Producto.objects.filter(estado=True).get(pk=pk)
        except Registro_Producto.DoesNotExist:
            return Response({'error': 'Lote no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        inventarioLote.estado=False # Eliminado logico
        inventarioLote.save()
        return Response(status=status.HTTP_204_NO_CONTENT) 
        