from django.urls import path
from .views import ClienteApiview,ClienteIDAPIView

app_name= "Clientes"

urlpatterns= [
    path("",ClienteApiview.as_view(),name="Clientes"),
    path('<int:pk>',ClienteIDAPIView.as_view())
]