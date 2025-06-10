
from rest_framework import viewsets
from goods_app.models  import Product, Category,Brand,Review
from goods_app.serializers import CategorySerializer, ProductSerilizer, ReviewSerializer


class ProductView(viewsets.ModelViewSet):
   queryset=Product.objects.all()
   serializer_class=ProductSerilizer

class CategoryViewSet(viewsets.ModelViewSet):
   queryset=Category.objects.all()
   serializer_class=ProductSerilizer

class ReviewViewSet(viewsets.ModelViewSet):
   queryset=Review.objects.all()
   serializer_class=ReviewSerilizer

class BrandReviewSet(viewsets.ModelViewSet):
   queryset=Brand.objects.all()
   serializer_class=ProductSerilizer





