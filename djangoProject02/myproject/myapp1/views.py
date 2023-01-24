from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.

products = {
    'telefon': ['İphone 13 Pro', 'Xioami Redmi 11'],
    'bilgisayar': ['Monster Notebook Abra Series', 'Monster Notebook Tulpar Series'],
    'elektronik': []
}

def index(request):
    htmlFilePath = 'myapp1/index.html'
    return render(request, htmlFilePath, {
        'product': products
    })
    
def product(request, productName):
    try:
        productText = products[productName]
        htmlFilePath = 'myapp1/product.html'
        return render(request, htmlFilePath, {
            'productsNames': productText,
            'namee': productName
        })
    except:
        return HttpResponseNotFound('Yanlış Kategori Seçimi!')