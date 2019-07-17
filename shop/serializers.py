from rest_framework import serializers

import shop.models


class CategorySerializer(serializers.ModelSerializer):
    number_of_items = serializers.IntegerField()
    number_of_subcategories = serializers.IntegerField()

    class Meta:
        model = shop.models.Category
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = shop.models.Item
        fields = '__all__'
