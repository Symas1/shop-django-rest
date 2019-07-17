import django_filters.rest_framework
from django import shortcuts
from rest_framework import filters
from rest_framework import permissions
from rest_framework import response
from rest_framework import viewsets

import shop.models
import shop.permissions
import shop.serializers


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = shop.models.Category.objects.all()
    serializer_class = shop.serializers.CategorySerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = shop.models.Item.objects.all()
    serializer_class = shop.serializers.ItemSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          shop.permissions.IsOwnerOrReadOnly]
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ('owner__username', 'category',)
    ordering_fields = ('price', 'number_of_views', 'created_at',)

    # def list(self, request, *args, **kwargs):
    # """
    # increases number_of_views counter each time all items are loaded
    # """
    #     self.queryset.update(number_of_views=models.F('number_of_views') + 1)
    #     serializer = shop.serializers.ItemSerializer(self.queryset, many=True)
    #     return response.Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        item = shortcuts.get_object_or_404(shop.models.Item.objects.all(), pk=kwargs['pk'])
        item.number_of_views += 1
        item.save()
        serializer = shop.serializers.ItemSerializer(item)
        return response.Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
