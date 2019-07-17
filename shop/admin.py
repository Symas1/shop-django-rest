from django.contrib import admin

import shop.models

admin.site.register(shop.models.Category)
admin.site.register(shop.models.Item)
