#from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics

from .models import Abonos
from .serializers import AbonoSerializer
#from drf_yasg.utils import swagger_auto_schema

'''class Abonolist (generics.ListAPIView):
    serializer_class = AbonoSerializer

    def get_queryset(self):
        return Abonos.objects.using('default').all()

'''

class AbonosApiView(APIView):
    def get(self, request):
     Serializer= AbonoSerializer(Abonos.objects.using('default').all(), many=True)
     return Response(status=status.HTTP_200_OK, data=Serializer.data)

      #departamento = list(Abono.objects.values())
       #return Response (status=status.HTTP_200_OK, data=departamento)

       #return Response(status=status.HTTP_200_OK, data= 'Hola mundo desde departamento')
        #return Response({'abonos': Abono.objects.all()})
    #forma 1 se va a trabajar con esta formas
   
    def post(self,request):
        Serializer= AbonoSerializer(data=request.data)
        Serializer.is_valid(raise_exception=True)
        Serializer.save()
        return Response (status=status.HTTP_201_CREATED, data=Serializer.data)

    """
    #forma 2
    def post2(self,request):
        Abono.objects.create(facturaid=request.data['facturaid'],monto=request.data['monto'],cajaid=request.data['cajaid'],Fecha_Abono=request.data['Fecha_Abono'])
        return Response (status=status.HTTP_201_CREATED)
    #forma 3
    def post3(self,request):
        abono= Abono

        abono.facturaid=request.data['facturaid']
        abono.monto=request.data['monto']
        abono.cajaid=request.data['cajaid']
        abono.Fecha_Abono=request.data['Fecha_Abono']
        abono.save()
        return Response (status=status.HTTP_201_CREATED)"""

        