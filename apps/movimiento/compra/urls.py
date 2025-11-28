from django.urls import path
from .views import CompraAPIView,CompraIDAPIView,DetallecompraAPIView,DetallecompraIDAPIView

app_name= "Compra"

urlpatterns= [
    path ("",CompraAPIView.as_view(), name="lista-compras"),
    path ("<int:pk>",CompraIDAPIView.as_view()),    
    path("detalles/",DetallecompraAPIView.as_view(), name="lista-detalles"),
    path("detalle/<int:pk>",DetallecompraIDAPIView.as_view())
]
