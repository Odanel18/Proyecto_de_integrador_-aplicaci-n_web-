from django.urls import path, include


urlpatterns = [

 path("abonos/", include('apps.movimiento.abono.urls')),
 path("caja/", include('apps.movimiento.caja.urls')),
 path ("compras/",include('apps.movimiento.compra.urls',namespace='compra')),
 path ("compras/", include('apps.movimiento.compra.urls',namespace='detalles')),
 path("factura/",include('apps.movimiento.factura.urls')),
 path("factura/",include('apps.movimiento.factura.urls', namespace='detalle/')),
 path("marcas/", include('apps.movimiento.marca.urls')),
 path("moto/", include('apps.movimiento.moto.urls')),
 path("productos/",include('apps.movimiento.producto.urls')),
 path("productos/",include('apps.movimiento.producto.urls', namespace='detalle')),


]
