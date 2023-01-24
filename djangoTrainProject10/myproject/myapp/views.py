from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
# Create your views here.

data = {
    'python': 'Python Kursuna Hoşgeldiniz!',
    'java': 'Java Kursuna Hoşgeldiniz!',
    'html': 'Html Kursuna Hoşgeldiniz!',
    'css': 'Css Kursuna Hoşgeldiniz!'
}

def index(request):
    htmlFilePath = "myapp/index.html"
    return render(request, htmlFilePath, {
        'datas': data
    })
    

def categoriesId(request, categoryId):
    return redirect("/python")


def categories(request, category):
    text = data[category]
    return HttpResponse(text)


    