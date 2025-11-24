from django.urls import path
from .views import EmpleadosAPIView,EmpleadoIDAPIView

#app_name= "Empleados"

urlpatterns = [
    path('',EmpleadosAPIView.as_view()),
    path('<int:pk>',EmpleadoIDAPIView.as_view())
]