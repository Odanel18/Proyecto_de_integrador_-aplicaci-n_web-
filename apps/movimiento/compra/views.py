from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.exceptions import ValidationError

from .models import Compras,DetalleCompra,ComprasCredito
from .serializers import CompraSerializer,DetalleCompraSerializer,CompraCreditoSerialezer
from drf_yasg.utils import swagger_auto_schema

from apps.movimiento.compra.service.compra_validacion import validar_compra,aumentar_stock

from django.db import transaction

from apps.movimiento.compra.service.validaciones import (
    validar_datos,
    resolver_detalle_producto,
    calcular_subtotal,
    suma_total,
    aumentar_stock,
)

class CompraAPIView (APIView):
    @swagger_auto_schema(responses={200: CompraSerializer(many=True)})
    def get(self,request):
        Serializer= CompraSerializer(Compras.objects.using('default').filter(estado=True).order_by('-id'), many=True)
        return Response(status=status.HTTP_200_OK, data=Serializer.data)
    
    @swagger_auto_schema(request_body=CompraSerializer, responses={201: CompraSerializer})
    def post(self, request):
        """
        Crea la compra junto con todos sus detalles en una sola llamada,
        siguiendo el mismo enfoque que el módulo de Factura:

        1. Se valida la cabecera de la compra con el serializer.
        2. Se crea la compra.
        3. Por cada producto del detalle se valida la cantidad/precio,
           se identifica el producto (por id, o por nombre/código +
           marca/moto/talla si hace falta desambiguar), se calcula el
           subtotal, se crea el DetalleCompra y se aumenta el stock
           generando un nuevo lote de inventario.
        4. Se calcula el total final de la compra.

        Todo el proceso ocurre dentro de una transacción atómica: si algo
        falla, no queda ningún dato a medias en la base de datos.
        """
        serializer = CompraSerializer(data=request.data)

        if serializer.is_valid():
            try:
                with transaction.atomic():
                    proveedor = serializer.validated_data.get('ProveedoresId')
                    condicion = serializer.validated_data.get('condicionId')
                    estado_cuenta = serializer.validated_data.get('estadoCuentaId')
                    num_compra = serializer.validated_data.get('NumCompra')
                    fecha = serializer.validated_data.get('Fecha')

                    detalles_data = request.data.get('detalles', [])

                    if not detalles_data:
                        raise ValidationError({"detalles": "Debes incluir al menos un producto en la compra."})

                    compra = Compras.objects.create(
                        NumCompra=num_compra,
                        Fecha=fecha,
                        Total=0,
                        ProveedoresId=proveedor,
                        condicionId=condicion,
                        estadoCuentaId=estado_cuenta,
                    )

                    for item in detalles_data:
                        # 1. Validamos cantidad y precio unitario
                        validar_datos(item)

                        # 2. Identificamos el producto: el usuario ya no
                        # necesita mandar el id, puede mandar el nombre o
                        # código del producto (y marca/moto/talla si hace
                        # falta para desambiguar variantes).
                        detalle_producto = resolver_detalle_producto(item)

                        cantidad = item['Cantidad']
                        precio_unitario = item['PrecioUnitario']
                        subtotal = calcular_subtotal(cantidad, precio_unitario)

                        DetalleCompra.objects.create(
                            Cantidad=cantidad,
                            PrecioUnitario=precio_unitario,
                            Subtotal=subtotal,
                            detallProductoId=detalle_producto,
                            CompraId=compra,
                        )

                        # 3. Cada compra genera un nuevo lote de inventario
                        aumentar_stock(detalle_producto.id, cantidad, precio_unitario)

                    # 4. Calculamos el total final de la compra
                    suma_total(compra.id)
                    compra.refresh_from_db()

                compra_serializer = CompraSerializer(compra)
                return Response(compra_serializer.data, status=status.HTTP_201_CREATED)

            except ValidationError as e:
                return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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