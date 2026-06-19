from .views import dimClienteListAPIView, dimCondicionPagoListAPIView, dimEmpleadoListAPIView, dimMetodoPagoListAPIView, dimProductoListAPIView, dimTiempoListAPIView, FactVentaListAPIView
from django.urls import path

app_name= 'ventas'

urlpatterns = [
    path('dimcliente/', dimClienteListAPIView.as_view()),
    path('dimcondicion/', dimCondicionPagoListAPIView.as_view()),
    path('dimempledo/', dimEmpleadoListAPIView.as_view()),
    path('dimmetodopago/', dimMetodoPagoListAPIView.as_view()),
    path('dimproducto/', dimProductoListAPIView.as_view()),
    path('dimtiempo/', dimTiempoListAPIView.as_view()),
    path('factventa/', FactVentaListAPIView.as_view()),
]