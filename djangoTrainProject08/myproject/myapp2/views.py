from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

data = {
    'temel kavramlar': 'Temel Kavramlar Konusuna Hoşgeldiniz!',
    'üslü sayılar': 'Üslü Sayılar Konusuna Hoşgeldiniz!',
    'köklü sayılar': 'Köklü Sayılar Konusuna Hoşgeldiniz!'
}

def index(request):
    htmlFilePath = 'myapp2/index.html'
    return render(request, htmlFilePath, {
        'datas': data
    })

def math(request, field):
    text = data[field]
    return HttpResponse(text)