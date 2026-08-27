from django.urls import path
from .views import ProveedorAPIView, ProveedorIDAPIView

app_name='proveedores'
urlpatterns=[
    path ('',ProveedorAPIView.as_view()),
    path ('<int:pk>',ProveedorIDAPIView.as_view())
]