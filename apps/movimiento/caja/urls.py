from django.urls import path
from .views import CajaApiView,CajaIDAPIView
#from django.contrib.auth.views import LoginView

app_name = "caja"

urlpatterns = [
   path("",CajaApiView.as_view(),name="Caja"),
   path('<int:pk>', CajaIDAPIView.as_view())
 ]