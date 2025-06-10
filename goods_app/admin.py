from django.contrib import admin
from .models import (
    Product,Category,ProductImage,
    Review,ReviewImage,ProductAttribute,Brand,Attribute,Questions
)

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(ProductImage)
admin.site.register(Review)
admin.site.register(ReviewImage)
admin.site.register(ProductAttribute)
admin.site.register(Brand)
admin.site.register(Attribute)
admin.site.register(Questions)

# Register your models here.
