from django.urls import path
from . import views

urlpatterns = [
    path('<str:categories>', views.index),
]