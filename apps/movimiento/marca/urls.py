from django.urls import path
from .views import MarcaAPIView,MarcaIDAPIView

app_name= 'marcas'

urlpatterns= [
    path("",MarcaAPIView.as_view(),name='marcas'),
    path('<int:pk>',MarcaIDAPIView.as_view())
]