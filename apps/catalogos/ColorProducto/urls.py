from django.urls import path
from .views import ColorProductoApiview, ColorProductoIDAPIView

app_name = "ColorProducto"

urlpatterns = [
    path('', ColorProductoApiview.as_view(), name='colores-producto'),
    path('<int:pk>', ColorProductoIDAPIView.as_view()),
]