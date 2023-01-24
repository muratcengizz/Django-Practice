from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('python', views.python),
    path('css', views.css),
    path('html', views.html),
    path('<int:fields>', views.intFields),
    path('<str:fields>', views.strFields)
]