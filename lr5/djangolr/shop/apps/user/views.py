from django.shortcuts import render
from django.http import JsonResponse

from django.views.decorators.http import require_http_methods

def shop_profile(request):
	return JsonResponse({'Заглушка' : 'Заглушка для профиля!'})