from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Facturas,DetalleFactura
from .serializers import FacturaSerializer,DetalleFacturaSerializer
from drf_yasg.utils import swagger_auto_schema
#logica validacines
from.services.factura_service import descontar_stock

class FacturaAPIView (APIView):
    @swagger_auto_schema(responses={200: FacturaSerializer(many=True)})
    def get (self,request):
        serializer= FacturaSerializer(Facturas.objects.filter(estado=True), many = True)
        return Response (data=serializer.data)
    
    @swagger_auto_schema(request_body=FacturaSerializer, responses={201: FacturaSerializer})
    def post(self,request):
       
       
       serializer=FacturaSerializer(data=request.data)
       serializer.is_valid(raise_exception=True)
       serializer.save()
       return Response(status=status.HTTP_201_CREATED,data=serializer.data)


class FacturaIDAPIView(APIView):
    
    @swagger_auto_schema(request_body=FacturaSerializer, responses={200: FacturaSerializer})
    def patch(self, request, pk):
        """
        Actualizar parcialmente un departamento por su ID.
        """
        try:
            factura = Facturas.objects.filter(estado=True).get(pk=pk)
        except Facturas.DoesNotExist:
            return Response({'error': 'Factura no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        serializer = FacturaSerializer(factura, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        """
        Eliminar un departamento por su ID.
        """
        try:
            factura = Facturas.objects.filter(estado=True).get(pk=pk)
        except Facturas.DoesNotExist:
            return Response({'error': 'Factura no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        factura.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 


class DetalleFacturaAPIView (APIView):
    @swagger_auto_schema(responses={200: DetalleFacturaSerializer(many=True)})
    def get (self,request):
        serializer= DetalleFacturaSerializer(DetalleFactura.objects.filter(estado=True), many = True)
        return Response (data=serializer.data)
    
    @swagger_auto_schema(request_body=DetalleFacturaSerializer, responses={201: DetalleFacturaSerializer})
    def post(self,request):
       serializer=DetalleFacturaSerializer(data=request.data)
       serializer.is_valid(raise_exception=True)
       detalle = serializer.save()#Se guarda el detalle de la factura
       
       detalle_producto_id = detalle.detalleProductoId.id
       cantidad= detalle.Cantidad

       print("Detalle producto: ", detalle_producto_id)
       print("Cantidad: ",cantidad)

       #llamar el servicio
       descontar_stock( detalle_producto_id , cantidad)

       return Response(status=status.HTTP_201_CREATED,data=serializer.data)

