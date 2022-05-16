from django.shortcuts import render
from django.http import JsonResponse
from category.models import Category
from django.views.decorators.csrf import csrf_exempt

def categories(request):
	return JsonResponse({'Заглушка' : 'Заглушка для страницы категорий!'})
	
def category(request, id_category):
	response = {'Заглушка' : 'Заглушка для категории №%s' % id_category} 
	return JsonResponse(response)

def all_categories(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        return JsonResponse({
            'Category': list(categories.values())
        })

@csrf_exempt 
def add_category(request):
    if request.method == 'GET':
        return JsonResponse({"status": False, "msg": "Нужен POST запрос"})

    if request.method == 'POST':
        name = request.GET.get("category_name", None)
        if not name:
            return JsonResponse({"status": False, "msg": "Укажите имя категории"})

        duplicates = Category.objects.filter(title=name)
        if len(duplicates) > 0:
            return JsonResponse({"status": False, "msg": "Уже есть такой"})
            
        new_category = Category()
        new_category.title = name
        new_category.save()
        
        return JsonResponse({"status": True, "msg": "Категория добавлена"})