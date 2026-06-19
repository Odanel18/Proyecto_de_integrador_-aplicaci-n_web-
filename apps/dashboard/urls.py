from django.urls import path, include

urlpatterns = [
    path('ventas/', include('apps.dashboard.ventas.urls',namespace='dimcliente/')),
    path('ventas/', include('apps.dashboard.ventas.urls', namespace='dimcondicion/')),
    path('ventas/', include('apps.dashboard.ventas.urls', namespace='dimempleado/' )),
    path('ventas/', include('apps.dashboard.ventas.urls',namespace='dimmetodopago/')),
    path('ventas/', include('apps.dashboard.ventas.urls',namespace='dimproducto')),
    path('ventas/', include('apps.dashboard.ventas.urls', namespace='dimtiempo/')),
    path('ventas/', include('apps.dashboard.ventas.urls', namespace='factventa/')),
]