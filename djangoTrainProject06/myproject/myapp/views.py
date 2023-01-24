from pydoc import TextRepr
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound
from django.template import loader
# Create your views here.

myData = {
    'django': 'Django Kursuna Hoşgeldiniz!',
    'tensorflow': 'Tensorflow Kursuna Hoşgeldiniz!',
    'numpy': 'Numpy Kursuna Hoşgeldiniz!',
    'scapy': 'Scapy Kursuna Hoşgeldiniz!',
    'cyber security': 'Welcome to the Cyber Security Course!',
    'machine learning': 'Welcome to the Machine Learning Course!',
    'artificial intelligence': 'Welcome to the Artificial Intelligence Course!',
}



def index(request):
    return render(request, "myapp/index.html",{
        'datas': myData
    })

def python(request):
    return HttpResponse("Python Course!")

def css(request):
    return HttpResponse("Css Course!")

def html(request):
    return HttpResponse("HTML Course!")

def intFields(request, fields):
    textlist = list(myData.keys())
    if fields > len(textlist):
        return HttpResponseNotFound('Yanlış Kategori Seçimi!')
    else:
        path = textlist[fields - 1]
        return redirect(f"/{path}")

def strFields(request, fields):
    try:
        path = myData[fields]
        return HttpResponse(path)
    except:
        return HttpResponseNotFound('Yanlış kategori Seçimi!')
