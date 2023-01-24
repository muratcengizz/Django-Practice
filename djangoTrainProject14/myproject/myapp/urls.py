from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('<int:categoryId>', views.categoryId),
    path('<categoryInformation>', views.category, name='productByCategory')
]