from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django_filters.views import FilterView
from filters_app.filters import ProductFilter
from .models import Product, Category, ProductAttribute, Brand, Questions, Review, ReviewImage



class ProductListView(FilterView):
    model = Product
    template_name = 'goods_app/products.html'
    context_object_name = 'products'
    paginate_by = 32
    filterset_class = ProductFilter

    def get_queryset(self):
        queryset = super().get_queryset().select_related('category', 'brand').prefetch_related('images')

        category_slug = self.kwargs.get('category_slug')
        brand_slug = self.kwargs.get('brand_slug')

        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)
        if brand_slug:
            queryset = queryset.filter(brand__slug=brand_slug)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['brands'] = Brand.objects.all()

        category_slug = self.kwargs.get('category_slug')
        brand_slug = self.kwargs.get('brand_slug')

        if category_slug:
            context['current_category'] = Category.objects.get(slug=category_slug)
        if brand_slug:
            context['current_brand'] = Brand.objects.get(slug=brand_slug)

        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'goods_app/product.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Только атрибуты текущего продукта
        context['attributes'] = ProductAttribute.objects.filter(product=self.object)
        # Отзывы текущего продукта
        reviews = Review.objects.filter(product=self.object).prefetch_related('images')
        context['reviews'] = reviews
        # Отдельный QuerySet для изображений
        context['review_images'] = ReviewImage.objects.filter(review__in=reviews)
        return context

class QuestionsListView(ListView):
    model = Questions
    template_name = 'goods_app/questions.html'
    context_object_name = 'questions'


class QuestionsDetailView(DetailView):
    model = Questions
    template_name = 'goods_app/question.html'
    context_object_name = 'question'


class RegisterView:
    pass


class ProductViewSet:
    pass