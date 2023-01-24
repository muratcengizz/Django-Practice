from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:category>', views.getProductByCategoryId),
    path('<str:category>', views.getProductByCategory),
]