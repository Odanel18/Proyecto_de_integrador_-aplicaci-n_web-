from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Facturas,DetalleFactura,FacturasCredito
from .serializers import FacturaSerializer,DetalleFacturaSerializer,FacturaCreditoSerializer
from drf_yasg.utils import swagger_auto_schema
#logica validacines
from rest_framework.exceptions import ValidationError
from.services.factura_service import descontar_stock,validar_existencia,Validar_datos,suma_total
from django.db import transaction


#------------------------------
# FACTURA
#------------------------------
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



#------------------------------
# DETALLE FACTURA
#------------------------------


class DetalleFacturaAPIView (APIView):
    @swagger_auto_schema(responses={200: DetalleFacturaSerializer(many=True)})
    def get (self,request):
        serializer= DetalleFacturaSerializer(DetalleFactura.objects.filter(estado=True), many = True)
        return Response (data=serializer.data)
    
    @swagger_auto_schema(request_body=DetalleFacturaSerializer, responses={201: DetalleFacturaSerializer})
    @transaction.atomic
    def post(self,request):
       

       serializer=DetalleFacturaSerializer(data=request.data)

       if serializer.is_valid(raise_exception=True):
           try:
                datos = serializer.validated_data
                canti= datos['Cantidad']
                id_prod= datos["detalleProductoId"].id

                Validar_datos(datos)
                validar_existencia(id_prod,canti)

                detalle= serializer.save()

                detalle_producto_id = detalle.detalleProductoId.id
                cantidad= detalle.Cantidad
                factura_id= detalle.FacturaId.id
                
                
                suma_total(factura_id)
                descontar_stock(detalle_producto_id, cantidad)

                return Response(status=status.HTTP_201_CREATED,data=serializer.data)
           
           except ValidationError as e:
                return Response(e.detail,status=status.HTTP_400_BAD_REQUEST)
           except ValidationError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
               

       #serializer.is_valid(raise_exception=True)
       #detalle = serializer.save()#Se guarda el detalle de la factura
       
       #detalle_producto_id = detalle.detalleProductoId.id
       #cantidad= detalle.Cantidad

       #print("Detalle producto: ", detalle_producto_id)
       #print("Cantidad: ",cantidad)

       #llamar el servicio
       #descontar_stock( detalle_producto_id , cantidad)

       #return Response(status=status.HTTP_201_CREATED,data=serializer.data)

#------------------------------
# FACTURA AL CREDITO
#------------------------------


class FacturaCreditoAPIView (APIView):
    @swagger_auto_schema(responses={200: FacturaCreditoSerializer(many=True)})
    def get (self,request):
        serializer= FacturaCreditoSerializer(FacturasCredito.objects.filter(estado=True), many = True)
        return Response (data=serializer.data)
    
    @swagger_auto_schema(request_body=FacturaCreditoSerializer, responses={201: FacturaCreditoSerializer})
    def post(self,request):
       
       
       serializer=FacturaCreditoSerializer(data=request.data)
       serializer.is_valid(raise_exception=True)
       serializer.save()
       return Response(status=status.HTTP_201_CREATED,data=serializer.data)
    
class FacturaCreditoIDAPIView(APIView):
    
    @swagger_auto_schema(request_body=FacturaCreditoSerializer, responses={200: FacturaCreditoSerializer})
    def patch(self, request, pk):
        """
        Actualizar parcialmente un departamento por su ID.
        """
        try:
            facturaCred = FacturasCredito.objects.filter(estado=True).get(pk=pk)
        except FacturasCredito.DoesNotExist:
            return Response({'error': 'Factura al credito no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        serializer = FacturaSerializer(facturaCred, data=request.data, partial=True)
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
            facturaCred = FacturasCredito.objects.filter(estado=True).get(pk=pk)
        except FacturasCredito.DoesNotExist:
            return Response({'error': 'Factura al credito no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        facturaCred.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
