from django.contrib import admin
from .models import Product, ProductImage, ProductCategory

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "stock", "status", "created_at")


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ("id", "file", "created_at")


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at")


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
