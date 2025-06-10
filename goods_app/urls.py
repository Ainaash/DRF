from rest_framework.routers import DefaultRouter
from .views import  ProductViewSet, CategoryViewSet, ReviewViewSet,BrandReviewSet

router = DefaultRouter()

router.register(r'products',ProductViewSet,basename='product')
router.register(r'categories',CategoryViewSet,basename='category')
router.register(r'reviews',ReviewViewSet,basename='review')
router.register(r'brands',BrandReviewSet,basename='brand')

urlpatterns = router.urls