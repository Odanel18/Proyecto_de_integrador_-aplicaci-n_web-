from django.urls import path
from .views import OrigenSaldoApiview,OrigenSaldoIDAPIView

app_name= "OrigenSaldo"

urlpatterns= [
    path("",OrigenSaldoApiview.as_view(),name="OrigenSaldo"),
    path('<int:pk>',OrigenSaldoIDAPIView.as_view())
]