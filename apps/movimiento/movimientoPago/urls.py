from django.urls import path
from .views import MovimientoPagoApiview

urlpatterns=[
    path("",MovimientoPagoApiview.as_view()),
]