from django.urls import path
from .views import CategoriaApiView
#from django.contrib.auth.views import LoginView

app_name = "Categorias"

urlpatterns = [
   path("",CategoriaApiView.as_view(),name="Categoria"),
   #path('api/v1/abono', AbonosApiView.as_view(), name= "Abonos")
 ]