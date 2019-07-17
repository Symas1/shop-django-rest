from django.urls import path, include
from rest_framework import routers

import users.views

router = routers.DefaultRouter()
router.register('', users.views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
