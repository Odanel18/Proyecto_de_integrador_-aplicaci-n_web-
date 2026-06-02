from django.urls import path
from .views import CondicionPagoApiview,CondicionPagoIDAPIView

app_name= "CondicionPago"

urlpatterns= [
    path("",CondicionPagoApiview.as_view(),name="condionpago"),
    path('<int:pk>',CondicionPagoIDAPIView.as_view())
]