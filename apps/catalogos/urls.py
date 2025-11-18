from django.urls import path, include


urlpatterns = [

 #path("abonos/", include('apps.catalogos.abono.urls')),
 #path("caja/", include('apps.catalogos.caja.urls'))
  path("categoria/",include('apps.catalogos.categoria.urls'))
    ]
