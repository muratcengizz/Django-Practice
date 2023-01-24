from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:categoryId>', views.categoryIds),
    path('<str:categoryInfo>', views.category),
]