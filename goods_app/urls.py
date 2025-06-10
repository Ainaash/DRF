from rest_framework.routers import DefaultRouter
from .views import  ProductViewSet, CategoryViewSet, ReviewViewSet,BrandReviewSet

router = DefaultRouter()

router.register(r'products',ProductViewSet,basename='product')
router.register(r'categories',ProductViewSet,basename='category')
router.register(r'reviews',ProductViewSet,basename='review')
router.register(r'brands',ProductViewSet,basename='brand')

urlpatterns = router.urls