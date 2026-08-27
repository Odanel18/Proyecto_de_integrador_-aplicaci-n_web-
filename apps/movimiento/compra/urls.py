from django.urls import path
from .views import CompraAPIView,CompraIDAPIView

app_name= "Compra"

urlpatterns= [
    path ("",CompraAPIView.as_view(), name="lista-compras"),
    path ("<int:pk>",CompraIDAPIView.as_view())  
]
