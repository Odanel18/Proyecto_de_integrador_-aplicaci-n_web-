from django.urls import path
from .views import EstadoCuentaApiview,EstadoCuentaIDAPIView

app_name= "EstadoCuenta"

urlpatterns= [
    path("",EstadoCuentaApiview.as_view(),name="Clientes"),
    path('<int:pk>',EstadoCuentaIDAPIView.as_view())
]