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

from django.shortcuts import get_object_or_404
from .models import Clientes, CondicionPago,EstadoCuenta


#------------------------------
# FACTURA
#------------------------------
class FacturaAPIView (APIView):
    @swagger_auto_schema(responses={200: FacturaSerializer(many=True)})
    def get (self,request):
        serializer= FacturaSerializer(Facturas.objects.filter(estado=True), many = True)
        return Response (data=serializer.data)
    
    @swagger_auto_schema(request_body=FacturaSerializer)
    def post(self,request):
        serializer=FacturaSerializer(data=request.data)

        if serializer.is_valid():
            try:
                with transaction.atomic():
                    #numFactura= get_object_or_404(NumFactura, id=serializer.validated_data.get('NumFactura'))
                    cliente= get_object_or_404(Clientes, id=serializer.validated_data.get('ClienteId'))
                    condicion= get_object_or_404(CondicionPago, id=serializer.validated_data.get('condicionId'))
                    estadofactura= get_object_or_404(EstadoCuenta,id=serializer.validated_data.get('estadoCuentaId'))
                    numFactura = serializer.validated_data.get('NumFactura')
                    fecha= serializer.validated_data.get('Fecha')
                    detalles_data = serializer.validated_data.get('detalles')

                    factura= Facturas.objects.create(NumFactura= numFactura, Fecha =fecha, ClienteId= cliente, Total=0, condicionId= condicion, estadoCuentaId= estadofactura)
                   
                    for item in detalles_data:

                        id_prod= item["detalleProductoId"].id
                        canti= item['Cantidad']

                        subtotalv= id_prod.precio

                        validar_existencia(id_prod,canti)

                        detalle_serializer = DetalleFacturaSerializer(data={**item, "FacturaId": factura.id})

                        detalle_serializer.is_valid(raise_exception=True)

                        detalle= detalle_serializer.save()
                        
                        descontar_stock(detalle.detalleProductoId.id, detalle.Cantidad)

                        '''' DetalleFactura.objects.create(
                            Cantidad= canti,
                            Subtotal= 
                        )'''
                    
                    suma_total(factura.id)
                venta_seializer = FacturaSerializer(factura)
                return Response(venta_seializer.data, status=status.HTTP_201_CREATED)
               #return Response( FacturaSerializer(factura).data, status=status.HTTP_201_CREATED)

            except Exception as e:
                Response({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST )
    
    ''''@swagger_auto_schema(request_body=FacturaSerializer, responses={201: FacturaSerializer})
    def post(self,request):
       datos_factura= request.data
       detalles = datos_factura.pop("detalles", [])
       
       factura_serializer = FacturaSerializer(data=datos_factura)
       factura_serializer.is_valid(raise_exception=True)

       factura = factura_serializer.save()

       for item in detalles:
           id_prod= item["detalleProductoId"].id
           canti= item['Cantidad']

           validar_existencia(id_prod,canti)

           detalle_serializer = DetalleFacturaSerializer(data={**item, "FacturaId": factura.id})

           detalle_serializer.is_valid(raise_exception=True)

           detalle= detalle_serializer.save()
           
           descontar_stock(detalle.detalleProductoId.id, detalle.Cantidad)
        
       suma_total(factura.id)
       return Response( FacturaSerializer(factura).data, status=status.HTTP_201_CREATED)

       #serializer=FacturaSerializer(data=request.data)
       #serializer.is_valid(raise_exception=True)
       #serializer.save()'''


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
               

class DetallaeFacturaIDAPIView(APIView):
    
    @swagger_auto_schema(request_body=DetalleFacturaSerializer, responses={200: DetalleFacturaSerializer})
    def patch(self, request, pk):
        """
        Actualizar parcialmente un departamento por su ID.
        """
        try:
            detalleFact = DetalleFactura.objects.filter(estado=True).get(pk=pk)
        except FacturasCredito.DoesNotExist:
            return Response({'error': 'Detalle factura no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = DetalleFacturaSerializer(detalleFact, data=request.data, partial=True)
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
            detalleFact = DetalleFactura.objects.filter(estado=True).get(pk=pk)
        except DetalleFactura.DoesNotExist:
            return Response({'error': 'Detalle factura no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        detalleFact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 


#------------------------------
# FACTURA AL CREDITO
#------------------------------
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
