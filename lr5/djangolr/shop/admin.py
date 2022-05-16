from django.contrib import admin
from user.models import Profile
from product.models import Product
from category.models import Category

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')
    list_filter = ('first_name',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ('title',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ('title',)

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)