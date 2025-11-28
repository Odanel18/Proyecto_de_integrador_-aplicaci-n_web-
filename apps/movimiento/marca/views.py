from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Marcas
from .serializers import MarcaSerializer
from drf_yasg.utils import swagger_auto_schema

class MarcaAPIView (APIView):
    def get(self,resquest):
        serializer= MarcaSerializer(Marcas.objects.filter(estado=True), many=True)
        return Response(status=status.HTTP_200_OK,data=serializer.data)
    @swagger_auto_schema(request_body=MarcaSerializer, responses= {201: MarcaSerializer})
    def post(self, resquest):
       serializer=MarcaSerializer(data= resquest.data)
       serializer.is_valid(raise_exception=True)
       serializer.save()
       return Response(status=status.HTTP_201_CREATED, data=serializer.data)


class MarcaIDAPIView(APIView):    
    @swagger_auto_schema(request_body=MarcaSerializer, responses={200: MarcaSerializer})
    def patch(self, request, pk):
        try:
            empleado = Marcas.objects.filter(estado=True).get(pk=pk)
        except Marcas.DoesNotExist:
            return Response({'error': 'Marca no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = MarcaSerializer(empleado, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            marca = Marcas.objects.filter(estado=True).get(pk=pk)
        except Marcas.DoesNotExist:
            return Response({'error': 'Marca no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        marca.estado= False
        marca.save()
        return Response(status=status.HTTP_204_NO_CONTENT) 