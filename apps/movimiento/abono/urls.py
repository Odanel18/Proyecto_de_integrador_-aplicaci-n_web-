from django.urls import path
from .views import AbonosApiView
#from django.contrib.auth.views import LoginView

app_name = "Abonos"

urlpatterns = [
   path("",AbonosApiView.as_view(),name="Abonos"),
   #path('api/v1/abono', AbonosApiView.as_view(), name= "Abonos")
 ]