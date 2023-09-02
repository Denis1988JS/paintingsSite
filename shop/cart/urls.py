from django.contrib import admin
from django.urls import path, include,re_path
from .views import *

urlpatterns = [
    path('',cart, name='cart'),#Страница корзина покупок
    path('add_cart/<int:paint_id>',add_cart, name='add_cart'),#Страница добавление товара
    path('remove/<int:paint_id>', cart_remove, name='cart_remove'),#Удаление товара
    ]