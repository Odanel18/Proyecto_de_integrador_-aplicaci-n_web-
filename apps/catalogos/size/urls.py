from rest_framework.routers import DefaultRouter
from .views import SizeModelViewSet

router = DefaultRouter()
router.register(r'', SizeModelViewSet, basename='tipo')

urlpatterns = router.urls
