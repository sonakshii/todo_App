from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('delete/<int:n>', views.delete,name="delete"),
    path('add/', views.add,name="add"),
]