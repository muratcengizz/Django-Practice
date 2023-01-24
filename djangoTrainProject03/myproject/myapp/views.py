from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound

myData = {
    'python': 'Python Kursuna Hoşgeldiniz!',
    'html': 'HTML Kursuna Hoşgeldiniz!',
    'css': 'CSS Kursuna Hoşgeldiniz!',
    'django': 'Django Kursuna Hoşgeldiniz!',
    'tensorflow': 'Tensorflow Kursuna Hoşgeldiniz!',
    }

def index(request):
    return HttpResponse('İndex Sayfası!')

def getProductByCategoryId(request, category):
    myIds = list(myData.keys())
    if (category > len(myIds)):
        return HttpResponseNotFound('Yanlış İndex!')
    redirect_text = myIds[category - 1]
    return redirect('/' + redirect_text)


def getProductByCategory(request, category):
    return HttpResponse(myData[category])
    