from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

data = {
    "python": "Python Kursuna Hoşgeldiniz!",
    "html": "HTML Kursuna Hoşgeldiniz!",
    "css": "CSS Kursuna Hoşgeldiniz!",
    "django": "Django Kursuna Hoşgeldiniz!"
}

def index(request):
    categories= list(data.keys())
    return render(request, 'myapp/index.html', {
        'categories': categories
    })

def getProductByCategory(request):
    categories = list(data.keys())
    return HttpResponse(categories)

