from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:category>', views.categoriesId),
    path('<str:category>', views.categories)
]