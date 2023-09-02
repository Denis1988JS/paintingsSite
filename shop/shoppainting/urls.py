from django.contrib import admin
from django.urls import path, include,re_path
from .views import *
from django.views.decorators.cache import cache_page
urlpatterns = [
    path('',cache_page(10)(MainPage.as_view()), name='home'),#Все маршруты из приложения women
    path('about',aboutUs, name='aboutUs'),#Страница о нас
    path('<int:year>',PaintingsYear.as_view(), name='paintingsYear'),#Вывод картин по году
    path('paint/<slug:painting_slug>',DetailViewPaintings.as_view(), name='paint'), #Показать картину по слагу через модель
    path('employees',EmployeesPage.as_view(), name='employees'), #Сотрудники компании
    path('newPaintings',NewPaintings.as_view(), name='newPaintings'), #Новинки
    path('profile/registeruser', RegisterUserView.as_view(), name='register'),#Страница регистрация пользователя
    path('profile/loginuser', LoginUser.as_view(), name='loginuser'),#Страница авторизация пользователя
    path('profile/logout/', LogoutPage.as_view(), name='logout'),#Выход пользователя
    path('profile/user/<int:pk>/', UserProfile.as_view(), name='profile'),#Личный кабинет пользователя
    path('profile/user/changeUserInfo/', ChangeUserInfoView.as_view(), name='changeUserInfo'),#Изменения данных пользователя
    path('profile/user/сhangePasswordUser/', ChangePasswordUser.as_view(), name='сhangePasswordUser'),#Изменения пароля пользователя
    path('country/<str:country>',PaintingsCountry.as_view(), name='paintingsCountry'), #Показать картины по странам
    path('artists',EmployeesPageArtists.as_view(), name='artists'), #Художники компании
    path('menegers',EmployeesPageMenegers.as_view(), name='menegers'), #Менеджеры компании
    path('<slug:slug>',DetailEmployeesPage.as_view(), name='employee'), #Показать сотрудника
    path('products/products',ourProducts, name='products'), #Наша продукция
    path('reproductions/reproductions',Reproductions.as_view(), name='reproductions'), #Репродукции
]
