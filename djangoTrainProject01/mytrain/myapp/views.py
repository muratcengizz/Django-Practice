from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

data = {
    "telefon": "Telefon Kategorisi",
    "bilgisayar": "Bilgisayar Kategorisi",
    "elektronik": "Elektronik Kategorisi",
}

def index(request):
    return HttpResponse("İndex Sayfası!")

def getProductByCategoryId(request, category):
    return HttpResponse(f"{category} seçimi broo!")

def getProductByCategory(request, category):
    try:
        category_text = data[category]
        return HttpResponse(category_text)
    except:
        return HttpResponseNotFound("Yanlış Kategori Seçimi!")
