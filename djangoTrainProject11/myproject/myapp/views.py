from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

data = {
    'python': 'Python Kursuna Hoşgeldiniz!',
    'html': 'Html Kursuna Hoşgeldiniz!',
    'css': 'Css Kursuna Hoşgeldiniz!',
    'java': 'Java Kursuna Hoşgeldiniz!'
}

def index(request):
    categoryList = list(data.keys())
    return HttpResponse(categoryList)

def category(request, categoryInformation):
    categoryText = data[categoryInformation]
    return HttpResponse(categoryText)