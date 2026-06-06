from django.urls import path
from .views import CajaApiView,CajaIDAPIView,MovimientoCajaApiView,MovimientoCajaIDAPIView
#from django.contrib.auth.views import LoginView

app_name = "caja"

urlpatterns = [
   path("",CajaApiView.as_view(),name="Caja"),
   path('<int:pk>', CajaIDAPIView.as_view()),
   path("movimientoCaja/",MovimientoCajaApiView.as_view(),name="movimientoCaja"),
   path('movimientoCaja/<int:pk>', MovimientoCajaIDAPIView.as_view())
 ]