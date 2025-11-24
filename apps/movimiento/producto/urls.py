from django.urls import path
from .views import ProductoAPIView,ProductoIDAPIView,DetalleProductoAPIVew

app_name= "Productos"

urlpatterns=[
    path("",ProductoAPIView.as_view(), name= "Productos"),
    path('<int:pk>',ProductoIDAPIView.as_view()),
    path('destalle/',DetalleProductoAPIVew.as_view(), name="detalle")
]