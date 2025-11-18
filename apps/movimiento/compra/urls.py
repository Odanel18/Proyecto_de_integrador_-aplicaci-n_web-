from django.urls import path
from .views import CompraAPIView,DetallecompraAPIView

app_name= "compra"

urlpatterns= [
    path ("",CompraAPIView.as_view(), name="lista-compras"),
    path("detalles/",DetallecompraAPIView.as_view(), name="lista-detalles"),
]
