from django.urls import path
from .views import CompraAPIView,CompraIDAPIView,DetallecompraAPIView,DetallecompraIDAPIView,ComprasCreditoApiview, ComprasCreditoIDAPIView

app_name= "Compra"

urlpatterns= [
    path ("",CompraAPIView.as_view(), name="lista-compras"),
    path ("<int:pk>",CompraIDAPIView.as_view()),    
    path("detalles/",DetallecompraAPIView.as_view(), name="lista-detalles"),
    path("detalles/<int:pk>",DetallecompraIDAPIView.as_view()),
    path("compra_credito/",ComprasCreditoApiview.as_view()),
    path("compra_credito/<int:pk>",ComprasCreditoIDAPIView.as_view())
]
