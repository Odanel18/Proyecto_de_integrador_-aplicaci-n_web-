from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MovimientoPago
from .serializers import MovimientoPagoSerializer
from drf_yasg.utils import swagger_auto_schema

class MovimientoPagoApiview(APIView):

    @swagger_auto_schema(responses={200: MovimientoPagoSerializer(many=True)})
    def get(self, request):
        serializer = MovimientoPagoSerializer(MovimientoPago.objects.filter(estado=True), many=True)
        return Response(serializer.data)
    