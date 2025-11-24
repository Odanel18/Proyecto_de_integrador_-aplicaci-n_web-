from django.urls import path
from .views import MetodoPagoAPIView,MetodoPagoIDAPIView

app_name='MetodoPago'

urlpatterns=[
    path("",MetodoPagoAPIView.as_view(),name='MetodoPago'),
    path('<int:pk>',MetodoPagoIDAPIView.as_view())
]