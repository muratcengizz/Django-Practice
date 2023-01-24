from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.


data = {
    'python': ['django', 'tensorflow', 'numpy'],
    'html': ['body', 'head', 'container'],
    'css': [],
}


def index(request):
    htmlFilePath = 'index.html'
    return render(request, htmlFilePath, {
        'datas': data
    })
    

def categoryInput(request, category):
    try:
        htmlFilePath = f'products.html'
        categoryText = data[category]
        return render(request, htmlFilePath, {
            'categoryText': categoryText,
            'categoryInformation': category
        })
    except:
        return HttpResponseNotFound('Yanlış Kategori Seçimi!')

def categoryIdInput(request, categoryId):
    categoryList = list(data.keys())
    if categoryId > 0 and categoryId <= len(categoryList):
        categoryText = categoryList[categoryId - 1]
        redirectPath = f'/{categoryText}'
        return redirect(redirectPath)
    else:
        return HttpResponseNotFound("Yanlış Kategori Seçimi!")