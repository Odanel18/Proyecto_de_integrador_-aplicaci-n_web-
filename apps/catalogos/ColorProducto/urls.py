from django.urls import path
from .views import ColorProductoApiview, ColorProductoIDAPIView

urlpatterns = [
    path('', ColorProductoApiview.as_view(), name='colores-producto'),
    path('<int:pk>', ColorProductoIDAPIView.as_view()),
]

#urlpatterns = [
 #   path('colores-producto/', ColorProductoApiview.as_view(), name='colores-producto'),
  #  path('colores-producto/<int:pk>/', ColorProductoIDAPIView.as_view(), name='color-producto-detail'),
#]
