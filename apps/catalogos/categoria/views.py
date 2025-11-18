#from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Categorias
from .serializers import CategoriaSerializer

class CategoriaApiView(APIView):
    def get(self, request):
     Serializer= CategoriaSerializer(Categorias.objects.using('default').all(), many=True)
     return Response(status=status.HTTP_200_OK, data=Serializer.data)