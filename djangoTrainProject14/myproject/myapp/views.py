from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.

data = {
    'python': 'Python kursuna hoşgeldiniz!',
    'html': 'Html kursuna hoşgeldiniz!',
    'css': 'Css kursuna hoşgeldiniz!',
    'django': 'Django kursuna hoşgeldiniz!'
}


def index(request):
    htmlFilePath = 'index.html'
    return render(request, htmlFilePath, {
        'datas': data
    })
    
    
def category(request, categoryInformation):
    categoryText = data[categoryInformation]
    return HttpResponse(categoryText)

def categoryId(request, categoryId):
    categoryList = list(data.keys())
    categoryText = categoryList[categoryId - 1]
    redirectPath = 'products.html'
    return render(request, redirectPath, {
        'category': data[categoryText]
    })