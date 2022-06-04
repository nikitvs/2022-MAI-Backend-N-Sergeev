# from django.contrib import admin
# from .models import Product
# from .models import Category

# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('id', 'product_title')
#     list_filter = ('product_title',)

# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('id', 'category_text')
#     list_filter = ('category_text',)

# admin.site.register(Product, ProductAdmin)
# admin.site.register(Category, CategoryAdmin)
from django.contrib import admin

from .models import Product, Category

admin.site.register(Product)
admin.site.register(Category)