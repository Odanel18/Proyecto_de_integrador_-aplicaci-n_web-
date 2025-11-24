from rest_framework.routers import DefaultRouter
from .views import TipoModelViewSet

router = DefaultRouter()
router.register(r'', TipoModelViewSet, basename='tipo')

urlpatterns = router.urls
