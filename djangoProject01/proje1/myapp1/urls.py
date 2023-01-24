from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:category_id>', views.getProductByCategoryId),
    path('<str:category>', views.getProductsByCategory, name='products_by_category'),
]