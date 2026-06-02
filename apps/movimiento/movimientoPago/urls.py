from django.urls import path
from .views import MovimientoPagoteApiview,MovimientoPagoIDAPIView

app_name= "Clientes"

urlpatterns= [
    path("",MovimientoPagoteApiview.as_view(),name="MovimientoPago"),
    path('<int:pk>',MovimientoPagoIDAPIView.as_view())
]