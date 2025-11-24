from django.urls import path
from .views import AbonosApiView,AbonosIDAPIView
#from django.contrib.auth.views import LoginView

app_name = "Abonos"

urlpatterns = [
   path("",AbonosApiView.as_view(),name="Abonos"),
   path('<int:pk>', AbonosIDAPIView.as_view(), name= "Abonos")
 ]