from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('<int:categoryId>', views.categoryIdInput),
    path('<str:category>', views.categoryInput)
]