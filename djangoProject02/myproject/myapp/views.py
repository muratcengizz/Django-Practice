from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.

data = {
    'python': 'Python kursuna hoşgeldiniz!',
    'html': 'HTML kursuna hoşgeldiniz!',
    'css': 'CSS kursuna hoşgeldiniz!',
    'django': 'Django kursuna hoşgeldiniz!'
}

def index(request):
    htmlFilePath = 'myapp/index.html'
    return render(request, htmlFilePath, {
        'datas': data
    })


def category(request, categoryInfo):
    try:
        categoryName = data[categoryInfo]
        return HttpResponse(categoryName)
    except:
        return HttpResponseNotFound('Yanlış Kategori Seçimi!')
    
    
def categoryIds(request, categoryId):
    categoryList = list(data.keys())
    if categoryId > 0 and categoryId <= len(categoryList):
        categoryName = categoryList[categoryId - 1]
        return redirect(f'/{categoryName}')
    else:
        return HttpResponseNotFound('Yanlış Kategori Seçimi!')
