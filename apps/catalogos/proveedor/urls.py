from django.urls import path
from .views import ProveedorAPIView, ProveedorIDAPIView

urlpatterns=[
    path ('',ProveedorAPIView.as_view()),
    path ('<int:pk>',ProveedorIDAPIView.as_view())
]