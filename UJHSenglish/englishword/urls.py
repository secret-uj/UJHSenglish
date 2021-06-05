from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('select/', views.select, name='select'),
    path('input/', views.input, name='input'),
    path('skip/', views.skip, name='skip'),
    path('hint/', views.hint, name='hint'),
]