from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MetodoPago
from .serializers import MetodoPagoSerializer
from drf_yasg.utils import swagger_auto_schema

class MetodoPagoAPIView (APIView):
    def get(self,resquest):
        selializer= MetodoPagoSerializer(MetodoPago.objects.filter(estado=True), many=True)
        return Response (status=status.HTTP_200_OK, data=selializer.data)

class MetodoPagoIDAPIView(APIView):   
    @swagger_auto_schema(request_body=MetodoPagoSerializer, responses={200: MetodoPagoSerializer})
    def patch(self, request, pk):
        
        try:
            metodoPagos = MetodoPago.objects.filter(estado=True).get(pk=pk)
        except metodoPagos.DoesNotExist:
            return Response({'error': 'Metodo de pago no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = MetodoPagoSerializer(metodoPagos, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
      
        try:
            metodoPagos = MetodoPago.objects.filter(estado=True).get(pk=pk)
        except MetodoPago.DoesNotExist:
            return Response({'error': 'Metodo de pago no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        metodoPagos.estado=False # Eliminado logico
        metodoPagos.save()
        return Response(status=status.HTTP_204_NO_CONTENT) 