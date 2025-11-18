from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics

from .models import Caja
from .serializers import CajaSerializer
from drf_yasg.utils import swagger_auto_schema

'''class Abonolist (generics.ListAPIView):
    serializer_class = AbonoSerializer

    def get_queryset(self):
        return Abonos.objects.using('default').all()

'''

class CajaApiView(APIView):
    def get(self, request):
     Serializer= CajaSerializer(Caja.objects.using('default').all(), many=True)
     return Response(status=status.HTTP_200_OK, data=Serializer.data)
