from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:categoriesId>', views.getProductByCategoryId),
    path('<str:categories>', views.getProductByCategory)
]