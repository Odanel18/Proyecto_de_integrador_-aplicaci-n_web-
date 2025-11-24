from django.urls import path
from .views import CategoriaApiView,CategoriaIDAPIView

app_name = "Categorias"

urlpatterns = [
   path("",CategoriaApiView.as_view(),name="Categoria"),
   path("<int:pk>",CategoriaIDAPIView.as_view())
 ]