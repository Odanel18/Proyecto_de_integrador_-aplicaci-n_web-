from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Proveedores
from .serializers import ProveedorSerializer
from drf_yasg.utils import swagger_auto_schema

class ProveedorAPIView (APIView):
    @swagger_auto_schema(responses={200: ProveedorSerializer(many=True)})
    def get (self,request):
        serializer= ProveedorSerializer(Proveedores.objects.filter(estado=True), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    @swagger_auto_schema(request_body=ProveedorSerializer, responses= {201: ProveedorSerializer})
    def post (self,request):
        serializer= ProveedorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)
   
class ProveedorIDAPIView(APIView):


    @swagger_auto_schema(request_body=ProveedorSerializer, responses={200: ProveedorSerializer})
    def patch(self, request, pk):
   
        try:
            proveedor = Proveedores.objects.get(pk=pk)
        except Proveedores.DoesNotExist:
            return Response({'error': 'Proveedor no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProveedorSerializer(proveedor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No jContent'})
    def delete(self, request, pk):
     
        try:
            proveedor = Proveedores.objects.get(pk=pk)
        except Proveedores.DoesNotExist:
            return Response({'error': 'Proveedor no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        proveedor.estado=False # Eliminado logico
        proveedor.save()
        return Response(status=status.HTTP_204_NO_CONTENT) 