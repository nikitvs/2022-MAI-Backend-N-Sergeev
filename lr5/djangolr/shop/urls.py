from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', include('user.urls')),
    path('products_list/', include('product.urls')),
    path('categories/', include('category.urls')),
    path('category/', include('category.urls')),
]