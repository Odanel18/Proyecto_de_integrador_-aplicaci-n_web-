from .models import dimCliente,dimCondicionPago, dimEmpleado, dimMetodoPago, dimProducto, dimTiempo, FactVenta
from .serializers import dimClienteSerializer, dimCondicionPagoSerializer, dimEmpleadoSerializer, dimMetodoPagoSerializer, dimProductoSerializer, dimTiempoSerializer, FactVentaSerializer
from rest_framework import status,generics
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema


class dimClienteListAPIView(generics.ListAPIView):
    serializer_class = dimClienteSerializer

    def get_queryset(self):
        return dimCliente.objects.using('dashboard').all()

class dimCondicionPagoListAPIView(generics.ListAPIView):
    serializer_class = dimCondicionPagoSerializer

    def get_queryset(self):
        return dimCondicionPago.objects.using('dashboard').all()

class dimEmpleadoListAPIView(generics.ListAPIView):
    serializer_class = dimEmpleadoSerializer

    def get_queryset(self):
        return dimEmpleado.objects.using('dashboard').all()

class dimMetodoPagoListAPIView(generics.ListAPIView):
    serializer_class = dimMetodoPagoSerializer

    def get_queryset(self):
        return dimMetodoPago.objects.using('dashboard').all()

class dimProductoListAPIView(generics.ListAPIView):
    serializer_class = dimProductoSerializer

    def get_queryset(self):
        return dimProducto.objects.using('dashboard').all()

class dimTiempoListAPIView(generics.ListAPIView):
    serializer_class = dimTiempoSerializer

    def get_queryset(self):
        return dimTiempo.objects.using('dashboard').all()

class FactVentaListAPIView(generics.ListAPIView):
    serializer_class = FactVentaSerializer

    def get_queryset(self):
        return FactVenta.objects.using('dashboard').all()
