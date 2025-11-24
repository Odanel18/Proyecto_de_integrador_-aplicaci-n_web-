from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Productos, DetalleProductos
from .serialezers import ProductoSerializer,DetalleProductoSerializer
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
            producto = Productos.objects.get(pk=pk)
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
            producto = Productos.objects.get(pk=pk)
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

        