from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.exceptions import ValidationError

from .models import Compras,DetalleCompra,ComprasCredito
from .serializers import CompraSerializer,DetalleCompraSerializer,CompraCreditoSerialezer
from drf_yasg.utils import swagger_auto_schema

from apps.movimiento.compra.service.compra_validacion import validar_compra,aumentar_stock

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


        serializer = DetalleCompraSerializer(data= resquest.data)

        if serializer.is_valid(raise_exception=True):
            try:
                datos_validos = serializer.validated_data
                validar_compra(datos_validos)

                detalle=serializer.save()
                id_producto=detalle.detallProductoId.id
                canti= detalle.Cantidad
                precioUnitario=detalle.PrecioUnitario

                aumentar_stock(id_producto,canti,precioUnitario)
                
                return Response(status=status.HTTP_201_CREATED, data=serializer.data)
            except ValidationError as e:
                return Response(e.detail,status=status.HTTP_400_BAD_REQUEST)
            except ValidationError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


        #serializer.is_valid(raise_exception=True)
        #serializer.validated_data["Cantidad"]

        #cantidad = serializer.validated_data["Cantidad"]

        #compra_validacion(cantidad)

        #serializer.save()

        

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



class ComprasCreditoApiview (APIView):
     
    @swagger_auto_schema(responses={200: CompraCreditoSerialezer(many=True)})
    def get(self,request):
        serializer=CompraCreditoSerialezer(ComprasCredito.objects.filter(estado=True), many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(request_body=CompraCreditoSerialezer, responses={201: CompraCreditoSerialezer})
    def post(self,request):
       serializer=CompraCreditoSerialezer(data=request.data)
       serializer.is_valid(raise_exception=True)
       serializer.save()
       return Response(status=status.HTTP_201_CREATED,data=serializer.data)
    
class ComprasCreditoIDAPIView(APIView):   
    @swagger_auto_schema(request_body=CompraCreditoSerialezer, responses={200: CompraCreditoSerialezer})
    def patch(self, request, pk):
        
        try:
            compCredito = ComprasCredito.objects.filter(estado=True).get(pk=pk)
        except ComprasCredito.DoesNotExist:
            return Response({'error': 'Compra al credito no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CompraCreditoSerialezer(compCredito, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
      
        try:
            credito = ComprasCredito.objects.filter(estado=True).get(pk=pk)
        except ComprasCredito.DoesNotExist:
            return Response({'error': 'Compra al credito no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        credito.estado=False # Eliminado logico
        credito.save()
        return Response(status=status.HTTP_204_NO_CONTENT) 