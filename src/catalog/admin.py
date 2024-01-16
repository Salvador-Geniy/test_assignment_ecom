from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin

from catalog.models import CategoryModel, GoodModel, ImageModel, GoodVariations


class ImageInLine(admin.TabularInline):
    model = ImageModel


@admin.register(CategoryModel)
class CategoryModelAdmin(DjangoMpttAdmin):
    list_display = ('id', 'name')


@admin.register(GoodModel)
class GoodModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'created_at')
    inlines = [ImageInLine]
    ordering = ('category',)


@admin.register(ImageModel)
class ImageModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'good', 'img')


@admin.register(GoodVariations)
class GoodVariationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
