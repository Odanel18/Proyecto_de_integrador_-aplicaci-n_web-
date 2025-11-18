from django.urls import path
from .views import CajaApiView
#from django.contrib.auth.views import LoginView

app_name = "caja"

urlpatterns = [
   path("",CajaApiView.as_view(),name="Caja"),
   #path('api/v1/abono', AbonosApiView.as_view(), name= "Abonos")
 ]