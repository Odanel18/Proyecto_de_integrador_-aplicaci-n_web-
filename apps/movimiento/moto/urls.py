from django.urls import path
from .views import MotoApiview,MotoIDAPIView

urlpatterns= [
    path("",MotoApiview.as_view()),
    path ('<int:pk>',MotoIDAPIView.as_view())
]