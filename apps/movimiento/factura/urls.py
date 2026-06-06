from django.urls import path
from .views import FacturaAPIView,FacturaIDAPIView,DetalleFacturaAPIView,DetallaeFacturaIDAPIView,FacturaCreditoAPIView,FacturaCreditoIDAPIView

app_name= 'factura'
urlpatterns= [
    path ("",FacturaAPIView.as_view()),
    path ('<int:pk>',FacturaIDAPIView.as_view()),
    path ("detalle/",DetalleFacturaAPIView.as_view()),
    path ("detalle/<int:pk>",DetalleFacturaAPIView.as_view()),
    path("credito/",FacturaCreditoAPIView.as_view()),
    path("credito/<int:pk>",FacturaCreditoIDAPIView.as_view())

]