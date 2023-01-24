from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

my_data = {
    'python': "Python Kursuna Hoşgeldiniz!",
    'html': "HTML Kursuna Hoşgeldiniz!",
    'css': "CSS Kursuna Hoşgeldiniz!",
}

def index(request):
    return HttpResponse("İndex sayfası babacım!")

def getProductByCategoryId(request, category):
    ids = list(my_data.keys())
    return HttpResponse(ids[category-1])

def getProductByCategory(request, category):
    try:
        myData = my_data[category]
        return HttpResponse(myData)
    except:
        return HttpResponseNotFound('Yanlış Kategori Seçimi!')
