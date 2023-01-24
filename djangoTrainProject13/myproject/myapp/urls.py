from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:categoryId>', views.getCategoryId),
    path('<str:category>', views.getCategory)
]