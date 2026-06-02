
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import OrigenSaldo
from .serializers import OrigenSaldoSerializer
from drf_yasg.utils import swagger_auto_schema

class OrigenSaldoApiview (APIView):
     
    @swagger_auto_schema(responses={200: OrigenSaldoSerializer(many=True)})
    def get(self,request):
        serializer=OrigenSaldoSerializer(OrigenSaldo.objects.filter(estado=True), many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(request_body=OrigenSaldoSerializer, responses={201: OrigenSaldoSerializer})
    def post(self,request):
       serializer=OrigenSaldoSerializer(data=request.data)
       serializer.is_valid(raise_exception=True)
       serializer.save()
       return Response(status=status.HTTP_201_CREATED,data=serializer.data)
    
class OrigenSaldoIDAPIView(APIView):   
    @swagger_auto_schema(request_body=OrigenSaldoSerializer, responses={200: OrigenSaldoSerializer})
    def patch(self, request, pk):
        
        try:
            origenS = OrigenSaldo.objects.filter(estado=True).get(pk=pk)
        except OrigenSaldo.DoesNotExist:
            return Response({'error': 'No se encontrado origen de dinero'}, status=status.HTTP_404_NOT_FOUND)

        serializer = OrigenSaldoSerializer(origenS, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
      
        try:
            origenS = OrigenSaldo.objects.filter(estado=True).get(pk=pk)
        except OrigenSaldo.DoesNotExist:
            return Response({'error': 'No se encontrado origen de dinero'}, status=status.HTTP_404_NOT_FOUND)

        origenS.estado=False # Eliminado logico
        origenS.save()
        return Response(status=status.HTTP_204_NO_CONTENT) 