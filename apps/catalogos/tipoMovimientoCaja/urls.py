from django.urls import path
from .views import TipoMovimientoCajaAPIView, TipoMovimientoCajaIDAPIView

urlpatterns=[
    path ('',TipoMovimientoCajaAPIView.as_view()),
    path ('<int:pk>',TipoMovimientoCajaIDAPIView.as_view())
]