from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ColorProducto
from .serializers import ColorProductoSerializer
from drf_yasg.utils import swagger_auto_schema

class ColorProductoApiview (APIView):
     
    @swagger_auto_schema(responses={200: ColorProductoSerializer(many=True)})
    def get(self,request):
        serializer=ColorProductoSerializer(ColorProducto.objects.filter(estado=True).order_by('-id'), many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(request_body=ColorProductoSerializer, responses={201: ColorProductoSerializer})
    def post(self,request):
       serializer=ColorProductoSerializer(data=request.data)
       serializer.is_valid(raise_exception=True)
       serializer.save()
       return Response(status=status.HTTP_201_CREATED,data=serializer.data)


class ColorProductoIDAPIView(APIView):
    @swagger_auto_schema(request_body=ColorProductoSerializer, responses={200: ColorProductoSerializer})
    def patch(self, request, pk):
        
        try:
            color_producto = ColorProducto.objects.filter(estado=True).get(pk=pk)
        except ColorProducto.DoesNotExist:
            return Response({'error': 'Color de Producto no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ColorProductoSerializer(color_producto, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'Color de producto eliminado correctamente'})
    def delete(self,request,pk):
        try:
            color_producto = ColorProducto.objects.filter(estado=True).get(pk=pk)
        except ColorProducto.DoesNotExist:
            return Response({'error': 'Color de producto no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        color_producto.estado=False #Eliminado Logico
        color_producto.save()
        return Response(status=status.HTTP_204_NO_CONTENT)