from django.urls import path
from .views import ProductoAPIView,ProductoIDAPIView,DetalleProductoAPIVew,DetalleProductosIDAPIView,Registro_ProductoApiView,Registro_ProductoIDAPIView

app_name= "Productos"

urlpatterns=[
    path("",ProductoAPIView.as_view(), name= "Productos"),
    path('<int:pk>',ProductoIDAPIView.as_view()),
    path('destalle/',DetalleProductoAPIVew.as_view(), name="detalle"),
    path('destalle/<int:pk>',DetalleProductoAPIVew.as_view()),
    path('inventarioLote/',Registro_ProductoApiView.as_view()),
    path('inventarioLote/<int:pk>',Registro_ProductoIDAPIView.as_view())
]