from django.shortcuts import render
from django.http import JsonResponse
from product.models import Product

def products_list(request):
	return JsonResponse({'Заглушка' : 'Заглушка для списка продуктов!'})

def all_products(request):
    if request.method == 'GET':
        products = Product.objects.all()
        return JsonResponse({
            'Product': list(products.values())
        })

def find_product(request):
    if request.method == 'GET':

        product_name = request.GET.get("product_name", None)
        if not product_name:
            return JsonResponse({"status": False, "msg": "Укажите название продукта"})
        product = Product.objects.filter(title=product_name).values()
        return JsonResponse({
            'Product': list(product.values())
        })