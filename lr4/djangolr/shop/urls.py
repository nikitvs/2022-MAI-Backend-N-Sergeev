from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.shop_profile, name='profile'),
    path('products_list', views.products_list, name='products_list'),
    path('categories', views.categories, name='categories'),
    path('category/<int:id_category>/', views.category, name='category'),
]