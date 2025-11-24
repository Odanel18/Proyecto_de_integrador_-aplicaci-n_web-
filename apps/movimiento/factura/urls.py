from django.urls import path
from .views import FacturaAPIView,FacturaIDAPIView,DetalleFacturaAPIView

app_name= 'factura'
urlpatterns= [
    path ("",FacturaAPIView.as_view()),
    path ('<int:pk>',FacturaIDAPIView.as_view()),
    path ("detalle/",DetalleFacturaAPIView.as_view())

]