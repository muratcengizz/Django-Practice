from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.

data = {
    'python': 'Python Kursuna Hoşgeldiniz!',
    'html': 'HTML Kursuna Hoşgeldiniz!',
    'css': 'CSS Kursuna Hoşgeldiniz!'
}

def index(request):
    htmlFilePath = 'myapp/index.html'
    return render(request, htmlFilePath)

def getCategoryId(request, categoryId):
    categoryList = list(data.keys())
    categoryText = categoryList[categoryId - 1]
    return redirect(f'/{categoryText}')

def getCategory(request, category):
    categoryText = data[category]
    return HttpResponse(categoryText)