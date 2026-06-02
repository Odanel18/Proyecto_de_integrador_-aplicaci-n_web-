
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import EstadoCuenta
from .serializers import EstadoCuentaSerializer
from drf_yasg.utils import swagger_auto_schema

class EstadoCuentaApiview (APIView):
     
    @swagger_auto_schema(responses={200: EstadoCuentaSerializer(many=True)})
    def get(self,request):
        serializer=EstadoCuentaSerializer(EstadoCuenta.objects.filter(estado=True), many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(request_body=EstadoCuentaSerializer, responses={201: EstadoCuentaSerializer})
    def post(self,request):
       serializer=EstadoCuentaSerializer(data=request.data)
       serializer.is_valid(raise_exception=True)
       serializer.save()
       return Response(status=status.HTTP_201_CREATED,data=serializer.data)
    
class EstadoCuentaIDAPIView(APIView):   
    @swagger_auto_schema(request_body=EstadoCuentaSerializer, responses={200: EstadoCuentaSerializer})
    def patch(self, request, pk):
        
        try:
            estadoCuenta = EstadoCuenta.objects.filter(estado=True).get(pk=pk)
        except EstadoCuenta.DoesNotExist:
            return Response({'error': 'Estado de cuenta no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = EstadoCuentaSerializer(estadoCuenta, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
      
        try:
            estadoCuenta = EstadoCuenta.objects.filter(estado=True).get(pk=pk)
        except EstadoCuenta.DoesNotExist:
            return Response({'error': 'Estado de cuenta no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        estadoCuenta.estado=False # Eliminado logico
        estadoCuenta.save()
        return Response(status=status.HTTP_204_NO_CONTENT) 