from django.urls import path, include
from rest_framework import routers

import shop.views

router = routers.DefaultRouter()
router.register('categories', shop.views.CategoryViewSet)
router.register('items', shop.views.ItemViewSet,basename='Item')

urlpatterns = [
    path('', include(router.urls)),
]
