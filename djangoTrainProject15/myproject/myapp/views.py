from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    htmlFilePath = 'index.html'
    return render(request, htmlFilePath)