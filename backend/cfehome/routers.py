from rest_framework.routers import DefaultRouter

from products.viewsets import ProductViewSets #or ProductGenericViewSets

router = DefaultRouter()
router.register('products-abc', ProductViewSets, basename = 'products')
urlpatterns = router.urls