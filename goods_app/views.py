
from rest_framework import viewsets
from .models  import Product, Category,Brand,Review
from .serializers import CategorySerializer, ProductSerializer, ReviewSerializer, BrandSerializer

from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample, extend_schema_view
from drf_spectacular.types import OpenApiTypes



@extend_schema_view(
    list=extend_schema(
        summary='Получение списка продуктов',
        description='Описание получение списка продуктов',
        responses={
            200: ProductSerializer,
            400: 'Bad request',
            404: 'Not found',
        }
    ),
    create=extend_schema(
        summary='Создание продукта',
        description='Описание создание продукта',
        responses={
            201: ProductSerializer,
            400: 'Bad request',
            404: 'Not found',
        }
    ),
    retrieve=extend_schema(
        summary='Получение продукта',
        description='Описание получение продукта',
        responses={
            200: ProductSerializer,
            400: 'Bad request',
            404: 'Not found',
        }
    ),
    update=extend_schema(
        summary='Обновление продукта',
        description='Описание обновление продукта',
        responses={
            200: ProductSerializer,
            400: 'Bad request',
            404: 'Not found',
        }
    ),
    partial_update=extend_schema(
        summary='Частичное обновление продукта',
        description='Описание частичное обновление продукта',
        responses={
            200: ProductSerializer,
            400: 'Bad request',
            404: 'Not found',
        }
    ),
    destroy=extend_schema(
        summary='Удаление продукта',
        description='Описание удаление продукта',
        responses={
            204: "Успешное удаление",
            400: 'Bad request',
            404: 'Not found',
        }
    )
)
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





