from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Compras,DetalleCompra
from .serializers import CompraSerializer,DetalleCompraSerializer
from drf_yasg.utils import swagger_auto_schema

class CompraAPIView (APIView):
    def get(self,request):
        Serializer= CompraSerializer(Compras.objects.using('default').filter(estado=True), many=True)
        return Response(status=status.HTTP_200_OK, data=Serializer.data)
    def post(self, resquest):
       serializer=DetalleCompraSerializer(data= resquest.data)
       serializer.is_valid(raise_exception=True)
       serializer.save()
       return Response(status=status.HTTP_201_CREATED, data=serializer.data)


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


class DetalleCompraIdAPIView(APIView):
    # ... otras funciones (post, put) ...

    @swagger_auto_schema(responses={200: DetalleCompraSerializer()})
    def get(self, request, pk):
        """
        Obtener un detalle de compra específico por su ID.
        """
        try:
            # 1. USAR EL MODELO CORRECTO
            # Suponiendo que tu modelo de detalle de compra se llama DetalleCompra
            detalle_compra = DetalleCompra.objects.get(pk=pk)
            
        # 2. CAPTURAR LA EXCEPCIÓN CORRECTA
        except DetalleCompra.DoesNotExist: 
            return Response(
                {'error': 'Detalle de compra no encontrado'}, 
                status=status.HTTP_404_NOT_FOUND
            )
        
        # 3. USAR EL SERIALIZADOR CORRECTO
        serializer = DetalleCompraSerializer(detalle_compra)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
