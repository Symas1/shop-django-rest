from rest_framework import serializers

import shop.models
from . import models


class UserSerializer(serializers.ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(many=True, queryset=shop.models.Item.objects.all())

    class Meta:
        model = models.CustomUser
        fields = ('id', 'username', 'items')
