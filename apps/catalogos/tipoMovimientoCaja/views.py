from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TipoMovimientoCaja
from .serializers import TipoMovimientoCajaSerializer
from drf_yasg.utils import swagger_auto_schema

class TipoMovimientoCajaAPIView (APIView):
    @swagger_auto_schema(responses={200: TipoMovimientoCajaSerializer(many=True)})
    def get (self,request):
        serializer= TipoMovimientoCajaSerializer(TipoMovimientoCaja.objects.filter(estado=True), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    @swagger_auto_schema(request_body=TipoMovimientoCajaSerializer, responses= {201: TipoMovimientoCajaSerializer})
    def post (self,request):
        serializer= TipoMovimientoCajaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)
   
class TipoMovimientoCajaIDAPIView(APIView):


    @swagger_auto_schema(request_body=TipoMovimientoCajaSerializer, responses={200: TipoMovimientoCajaSerializer})
    def patch(self, request, pk):
   
        try:
            tipoCJ = TipoMovimientoCaja.objects.filter(estado=True).get(pk=pk)
        except TipoMovimientoCaja.DoesNotExist:
            return Response({'error': 'Ese tipo de entrada en caja no se encuentra'}, status=status.HTTP_404_NOT_FOUND)

        serializer = TipoMovimientoCajaSerializer(tipoCJ, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No jContent'})
    def delete(self, request, pk):
     
        try:
            tipoCJ = TipoMovimientoCaja.objects.filter(estado=True).get(pk=pk)
        except TipoMovimientoCaja.DoesNotExist:
            return Response({'error': 'Ese tipo de entrada en caja no se encuentra'}, status=status.HTTP_404_NOT_FOUND)

        tipoCJ.estado=False # Eliminado logico
        tipoCJ.save()
        return Response(status=status.HTTP_204_NO_CONTENT) 