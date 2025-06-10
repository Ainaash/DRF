
from rest_framework import viewsets
from goods_app.models  import Product, Category,Brand,Review
from goods_app.serializers import CategorySerializer, ProductSerializer, ReviewSerializer, BrandSerializer


class ProductViewSet(viewsets.ModelViewSet):
   queryset=Product.objects.all()
   serializer_class=ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
   queryset=Category.objects.all()
   serializer_class=CategorySerializer

class ReviewViewSet(viewsets.ModelViewSet):
   queryset=Review.objects.all()
   serializer_class=ReviewSerializer

class BrandReviewSet(viewsets.ModelViewSet):
   queryset=Brand.objects.all()
   serializer_class=BrandSerializer





