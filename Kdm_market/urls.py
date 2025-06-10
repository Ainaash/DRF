
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from goods_app.urls import router as goods_router

router = routers.DefaultRouter()

router.registry.extend(goods_router.registry)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

