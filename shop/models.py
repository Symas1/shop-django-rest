from django.db import models


class CategoryManager(models.Manager):
    """
    Adds number of items and number of subcategories to category objects
    """

    def get_queryset(self):
        return super().get_queryset().annotate(number_of_items=models.Count('items')).annotate(
            number_of_subcategories=models.Count('subcategories'))


class Category(models.Model):
    title = models.CharField(max_length=30, unique=True)
    description = models.TextField(blank=True, default='')
    parent_category = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL,
                                        related_name='subcategories')

    objects = CategoryManager()

    def __str__(self):
        return self.title


class Item(models.Model):
    title = models.CharField(max_length=30)
    owner = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='items')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True, default='')
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    number_of_views = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
