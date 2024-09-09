from django.contrib import admin
from catalog.models import (
    Products,
    ProductImages,
    ProductParameters
)


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    pass

@admin.register(ProductImages)
class ProductImagesAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductParameters)
class ProductParametersAdmin(admin.ModelAdmin):
    pass
