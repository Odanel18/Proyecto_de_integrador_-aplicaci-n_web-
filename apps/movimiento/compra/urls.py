from django.urls import path
from .views import CompraAPIView,DetallecompraAPIView,DetalleCompraIdAPIView

app_name= "Compra"

urlpatterns= [
    path ("",CompraAPIView.as_view(), name="lista-compras"),
    path("detalles/",DetallecompraAPIView.as_view(), name="lista-detalles"),
    path("<int:pk>",DetalleCompraIdAPIView.as_view())
]
