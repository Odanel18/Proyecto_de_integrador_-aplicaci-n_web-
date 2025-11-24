
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Motos
from .serializers import MotoSerializer
from drf_yasg.utils import swagger_auto_schema

class MotoApiview (APIView):
     
    @swagger_auto_schema(responses={200: MotoSerializer(many=True)})
    def get(self,request):
        serializer=MotoSerializer(Motos.objects.filter(estado=True), many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(request_body=MotoSerializer, responses={201: MotoSerializer})
    def post(self,request):
       serializer=MotoSerializer(data=request.data)
       serializer.is_valid(raise_exception=True)
       serializer.save()
       return Response(status=status.HTTP_201_CREATED,data=serializer.data)
    
class MotoIDAPIView(APIView):   
    @swagger_auto_schema(request_body=MotoSerializer, responses={200: MotoSerializer})
    def patch(self, request, pk):
        
        try:
            moto = Motos.objects.get(pk=pk)
        except Motos.DoesNotExist:
            return Response({'error': 'Moto no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = MotoSerializer(moto, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
      
        try:
            moto = Motos.objects.get(pk=pk)
        except Motos.DoesNotExist:
            return Response({'error': 'Moto no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        moto.estado=False # Eliminado logico
        moto.save()
        return Response(status=status.HTTP_204_NO_CONTENT) 