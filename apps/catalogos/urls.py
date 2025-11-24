from django.urls import path, include


urlpatterns = [
  path("categoria/",include('apps.catalogos.categoria.urls')),
  path("clientes/",include('apps.catalogos.clientes.urls')),
  path("empleados/",include('apps.catalogos.empleados.urls')),
  path("metodopago/", include('apps.catalogos.metodoPago.urls')),
  path("proveedor/",include('apps.catalogos.proveedor.urls')),
  path("size/",include('apps.catalogos.size.urls')),
  path("tipo/", include ('apps.catalogos.tipo.urls'))
    ]
