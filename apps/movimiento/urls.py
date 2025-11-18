from django.urls import path, include


urlpatterns = [

 path("abonos/", include('apps.movimiento.abono.urls')),
 path("caja/", include('apps.movimiento.caja.urls')),
 path ("compras/",include('apps.movimiento.compra.urls',namespace='compra')),
 path ("compras/detalle/", include('apps.movimiento.compra.urls'))

]
