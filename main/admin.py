from django.contrib import admin
from .models import *

# Для связки изображения с продуктом
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductSizeInline(admin.TabularInline):
    model = ProductSize
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'color'] # Поля, которые будут отображаться в админке
    list_filter = ['category', 'color']
    search_fields = ['name', 'color', 'description']
    prepopulated_fields = {'slug': ('name',)} # Мы будем вводить название продукта, а slug будет сгенерирован автоматически
    inlines = [ProductImageInline, ProductSizeInline] # Для связки изображений с продуктом

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

class SizeAdmin(admin.ModelAdmin):
    list_display = ['name']

# Регистрация моделей, Берем модль и привязываем к ней настройки
admin.site.register(Category, CategoryAdmin),
admin.site.register(Product, ProductAdmin),
admin.site.register(Size, SizeAdmin),
