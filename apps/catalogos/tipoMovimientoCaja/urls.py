from django.urls import path
from .views import TipoMovimientoCajaAPIView, TipoMovimientoCajaIDAPIView

app_name = 'TipoMovimientoCaja'

urlpatterns=[
    path ('',TipoMovimientoCajaAPIView.as_view()),
    path ('<int:pk>',TipoMovimientoCajaIDAPIView.as_view())
]