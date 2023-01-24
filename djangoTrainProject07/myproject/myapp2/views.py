from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

data = {
    'temel bilgiler': 'Temel bilgiler konusuna hoşgeldiniz!',
    'üslü sayılar': 'Üslü sayılar konusuna hoşgeldiniz!',
    'köklü sayılar': 'Köklü sayılar konusuna hoşgeldiniz!'
}

def index(request):
    htmlFilePath = "myapp2/index.html"
    return render(request, htmlFilePath, {
        "datas": data
    })

def math(request, field):
    text = data[field]
    return HttpResponse(text)