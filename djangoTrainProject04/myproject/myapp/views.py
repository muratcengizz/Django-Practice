from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.

data = {
    "python": "Python Kursuna Hoşgeldiniz!",
    "html": "HTML Kursuna Hoşgeldiniz!",
    "css": "CSS Kursuna Hoşgeldiniz!",
    "django": "Django Kursuna Hoşgeldiniz!"
}

def index(request):
    categories_list = list(data.keys())
    return render(request, 'myapp/index.html', {
        'categories': categories_list
    })

def getProductByCategory(request, categories):
    categories_list = list(data.keys())
    if categories > len(categories_list):
        return HttpResponseNotFound("Yanlış İndex!")
    return render(request, 'myapp/products.html', {
        "category": "categories_list"
    })

def getProductByCategoryId(request, categoriesId):
    categories_list = list(data.keys())
    return HttpResponse(categories_list[categoriesId - 1])