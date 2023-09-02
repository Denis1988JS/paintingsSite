from django.db import models
from django.urls import reverse, reverse_lazy

#Валидаторы - дополнительно
from django.core.exceptions import ValidationError
from django.core import validators
import re
from datetime import datetime
def ValidateFormatPaintingSize(size):
    pattern = r"^[0-9]{2,3}x[0-9]{2,3}$"
    p = re.compile(pattern)
    rezult = p.search(size)
    if not rezult:
        raise ValidationError('Введите значение согластно шаблона 00x00 или 000x000')



# Create your models here.

#Создание моделей

#Модель - страна картины
class CountryPainting(models.Model):
    name_country = models.CharField(max_length=50, verbose_name='Страна')
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='URL-country')

    def __str__(self):#Вывод название страны
        return f'{self.name_country}'
    def get_absolute_url(self):#Ссылка на url по слагу
        return reverse('country', kwargs={'country_slug':self.slug})
    class Meta:#Для админки
        verbose_name = 'Страна'  # ед
        verbose_name_plural = 'Страны'  # множ

#Модель - формат картины
class FormatPainting(models.Model):
    canvas = models.CharField(max_length=50, unique=True, verbose_name='Материал')
    size = models.CharField(max_length=15, verbose_name='Размер',help_text='Размер в формате 00x00 или 000x000', validators=[
        ValidateFormatPaintingSize], error_messages={'invalid':'Введите в формате 00x00 или 000x000'})
    def __str__(self):#Вывод название страны
        return f'{self.canvas} {self.size}'
    class Meta:#Для админки
        verbose_name = 'Характеристика картины'  # ед
        verbose_name_plural = 'Характеристики картин'  # множ

#Модель - картина
class Painting(models.Model):
    name = models.CharField(max_length=75, verbose_name='Название')
    slug = models.SlugField(max_length=75, verbose_name='URL-картины')
    autor = models.CharField(max_length=75, verbose_name='Автор')
    year = models.IntegerField(verbose_name='Год',)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    formPaint = models.ForeignKey(FormatPainting, on_delete=models.CASCADE, verbose_name='Формат картины')
    countryPaint = models.ForeignKey(CountryPainting, on_delete=models.CASCADE, verbose_name='Страна картины')
    avaliable = models.BooleanField(default=True, db_index=True, verbose_name='Наличие')
    imagePainting = models.ImageField(upload_to="photos/painting/%Y/%m/%d/",verbose_name='Фото картины',)
    def __str__(self):#Вывод название страны
        return f'{self.name}'
    def get_absolute_url(self):#Ссылка на url по слагу
        return reverse('paint', kwargs={'painting_slug':self.slug})
    class Meta:#Для админки
        verbose_name = 'Картина'  # ед
        verbose_name_plural = 'Картины'  # множ

#Модель пользователя - обычный пользователь

from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
class BuyerUser(AbstractUser):
    is_active = models.BooleanField(default=True, db_index=True, verbose_name='Активный пользователь')
    phone_number = PhoneNumberField(unique = True, null = False, blank = False, verbose_name='Номер телефона')
    user_avatar = models.ImageField(upload_to="photos/users_avatar/%Y/%m/%d/",verbose_name='Аватарка пользователя',)
    def __str__(self):#Вывод название страны
        return f'{self.username}'
    # def get_absolute_url(self):#Ссылка на url по слагу
    #     return reverse('profile/user', kwargs={'username':self.username})
    class Meta:#Для админки
        verbose_name = 'Пользователь'  # ед
        verbose_name_plural = 'Пользователи'  # множ

#Модель отображения сотрудников - классы должность и характеристика сотрудника
class JobTitle(models.Model):
    nameJobTitle = models.CharField(max_length=50, verbose_name='Должность')
    slug = models.SlugField(max_length=50, verbose_name='URL-по должностям')

    def __str__(self):  # Вывод название страны
        return f'{self.nameJobTitle}'

    def get_absolute_url(self):  # Ссылка на url по слагу
        return reverse('employee/JobTitle', kwargs={'employee/JobTitle': self.slug})
    class Meta:#Для админки
        verbose_name = 'Должность'  # ед
        verbose_name_plural = 'Должности'  # множ

#Модель сотрудник компании
class Employee(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя сотрудника')
    slug = models.SlugField(max_length=30, verbose_name='URL-сотрудника')
    second_name = models.CharField(max_length=30, verbose_name='Фамилия сотрудника')
    thirt_name = models.CharField(max_length=30, verbose_name='Отчество сотрудника')
    phone_number = PhoneNumberField(unique=True, null=False, blank=False, verbose_name='Номер телефона')
    employee_avatar = models.ImageField(upload_to="photos/employee/%Y/%m/%d/", verbose_name='Аватарка сотрудника', )
    employee_content = models.TextField(max_length=5000, verbose_name='О сотруднике')
    JobTitle = models.ForeignKey(JobTitle, on_delete=models.CASCADE, related_name='JobTitle')
    def __str__(self):  # Вывод название страны
        return f'{self.second_name} {self.name} {self.thirt_name}'
    def get_absolute_url(self):  # Ссылка на url по слагу
        return reverse_lazy('employee', kwargs={'slug': self.slug})
    class Meta:#Для админки
        verbose_name = 'Сотрудник'  # ед
        verbose_name_plural = 'Сотрудники'  # множ

























