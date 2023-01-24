from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.template import loader
import datetime

data = {
    "telefon":    ["iphone 8", "iphone 11", "iphone 12"],
    "bilgisayar": ["monster notebook abra series", "monster notebook tulpar series"],
    "elektronik": [],
}

def index(request):
    categories = list(data.keys())
    return render(request, 'myapp1/index.html', {
        "categories": categories,
    })



def getProductByCategoryId(request, category_id):
    category_list = list(data.keys())
    if category_id > len(category_list):
        return HttpResponseNotFound("<h1>Yanlış Kategori Seçimi!</h1>")
    
    category_name = category_list[category_id - 1]
    redirect_path = reverse('products_by_category', args=[category_name])
    return redirect(redirect_path)



def getProductsByCategory(request, category):
    try:
        text = data[category]
        return render(request, 'myapp1/products.html', {
            "category": category,
            "category_text": text,
            "now": datetime.datetime.now,
        })
    except:
        return HttpResponseNotFound(f"<h1>Yanlış Kategori Seçimi!</h1>")