from django.urls import path
from .views import paintingsApi, paintingsDetailApi, employeesApi, employeeDetailApi, employeesMenegersApi, employeesArtistsApi, \
    paintingsYearApi, paintingsCountryApi, BuyerUserApiRegister, userProfileApi

urlpatterns = [
    path('paintingsApi/',paintingsApi),#Вывод всех картин
    path('paintingsApi/<int:pk>',paintingsDetailApi),#Вывод картины детально
    path('paintingsApi/year/<int:year>',paintingsYearApi),#Вывод картин по году
    path('paintingsApi/country/<str:country>',paintingsCountryApi),#Вывод картин по стране
    path('employees/',employeesApi),#Все сотрудники
    path('employees/<int:pk>',employeeDetailApi),#Сотрудник
    path('employees/artists',employeesMenegersApi),#Сотрудники менеджеры
    path('employees/menegers',employeesArtistsApi),#Сотрудники менеджеры
    path('apiRegister/', BuyerUserApiRegister.as_view()),#Регистрация пользователя/добавление новго пользователя
    path('userProfileApi/',userProfileApi),#Личный кабинет

]