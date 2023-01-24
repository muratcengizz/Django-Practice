from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.

data = {
    'python': 'Welcome to the Python course!',
    'css': 'Welcome to the Css course!',
    'html': 'Welcome to the Html course',
    'django': 'Welcome to the Django course!'
}

def index(request):
    htmlFilePath = "myapp1/index.html"
    return render(request, htmlFilePath, {
        'datas': data
    })

def software(request, field):
    text = data[field]
    return HttpResponse(text)

