from django.urls import path
from . import views

urlpatterns = [
    path('', views.products_list, name='products_list'),
    path('all', views.all_products, name='all_products'),
    path('find_product', views.find_product, name='find_product'),
]