
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CondicionPago
from .serializers import CondicionPagoSerializer
from drf_yasg.utils import swagger_auto_schema

class CondicionPagoApiview (APIView):
     
    @swagger_auto_schema(responses={200: CondicionPagoSerializer(many=True)})
    def get(self,request):
        serializer=CondicionPagoSerializer(CondicionPago.objects.filter(estado=True), many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(request_body=CondicionPagoSerializer, responses={201: CondicionPagoSerializer})
    def post(self,request):
       serializer=CondicionPagoSerializer(data=request.data)
       serializer.is_valid(raise_exception=True)
       serializer.save()
       return Response(status=status.HTTP_201_CREATED,data=serializer.data)
    
class CondicionPagoIDAPIView(APIView):   
    @swagger_auto_schema(request_body=CondicionPagoSerializer, responses={200: CondicionPagoSerializer})
    def patch(self, request, pk):
        
        try:
            condicion = CondicionPago.objects.filter(estado=True).get(pk=pk)
        except CondicionPago.DoesNotExist:
            return Response({'error': 'Condicion pago no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CondicionPagoSerializer(condicion, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
      
        try:
            condicion = CondicionPago.objects.filter(estado=True).get(pk=pk)
        except CondicionPago.DoesNotExist:
            return Response({'error': 'Condicion de pago no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        condicion.estado=False # Eliminado logico
        condicion.save()
        return Response(status=status.HTTP_204_NO_CONTENT) 