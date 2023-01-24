from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

data = {
    'Matamatik': 'Matamatik Konuları',
    'Yazılım': 'Yazılım Konuları'
}

def index(request):
    htmlFilePath = "baseFile/index.html"
    return render(request, htmlFilePath, {
        'datas': data
    })