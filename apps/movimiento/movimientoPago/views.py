
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MovimientoPago
from .serializers import MovimientoPagoSerializer
from drf_yasg.utils import swagger_auto_schema

class MovimientoPagoteApiview (APIView):
     
    @swagger_auto_schema(responses={200: MovimientoPagoSerializer(many=True)})
    def get(self,request):
        serializer=MovimientoPagoSerializer(MovimientoPago.objects.filter(estado=True), many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(request_body=MovimientoPagoSerializer, responses={201: MovimientoPagoSerializer})
    def post(self,request):
       serializer=MovimientoPagoSerializer(data=request.data)
       serializer.is_valid(raise_exception=True)
       serializer.save()
       return Response(status=status.HTTP_201_CREATED,data=serializer.data)

class MovimientoPagoIDAPIView(APIView):   
    @swagger_auto_schema(request_body=MovimientoPagoSerializer, responses={200: MovimientoPagoSerializer})
    def patch(self, request, pk):
        
        try:
            movimiento = MovimientoPago.objects.filter(estado=True).get(pk=pk)
        except movimiento.DoesNotExist:
            return Response({'error': 'Movimiento no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = MovimientoPagoSerializer(movimiento, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
      
        try:
            movimiento = MovimientoPago.objects.filter(estado=True).get(pk=pk)
        except MovimientoPago.DoesNotExist:
            return Response({'error': 'Cliente no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        movimiento.estado=False # Eliminado logico
        movimiento.save()
        return Response(status=status.HTTP_204_NO_CONTENT) 