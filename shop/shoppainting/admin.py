from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *
# Register your models here.

class PaintingInline(admin.TabularInline):#Горизонтальный встроенный модели Картины
    model = Painting
    classes = ('collapse',)
    extra = 1
class CountryPaintingAdmin(admin.ModelAdmin):#Модель страна картины в АДМИНКЕ
    list_display = ('name_country','slug',)
    list_display_links = ('name_country','slug',)
    search_fields = ('name_country','slug',)
    search_help_text = ('Поиск по странам')
    fields = ('name_country','slug',)
    prepopulated_fields = {'slug': ('name_country',)}
    inlines = (PaintingInline,)
admin.site.register(CountryPainting,CountryPaintingAdmin)


class FormatPaintingAdmin(admin.ModelAdmin):#Модель - формат картины в АДМИНКЕ
    list_display = ('canvas','size',)
    list_display_links = ('canvas', 'size',)
    search_fields = ('canvas', 'size',)
    inlines = (PaintingInline,)
admin.site.register(FormatPainting,FormatPaintingAdmin)


class PaintingAdmin(admin.ModelAdmin):#Модель - картины в Админке
    list_display = ('name', 'slug','autor','year','price','formPaint','countryPaint','avaliable','get_html_photo')
    list_display_links = ('name', 'slug')
    search_fields = ('name', 'autor')
    search_help_text = ('Поиск по картинам')
    list_editable = ('avaliable',)
    list_filter = ('avaliable','formPaint','countryPaint','year')
    prepopulated_fields = {'slug': ('name',)}
    def get_html_photo(self, object):
        if object.imagePainting:
            return mark_safe(f"<img src='{object.imagePainting.url}' width=35>")
    get_html_photo.short_description = 'Фото'
admin.site.register(Painting,PaintingAdmin)


class BuyerUserAdmin(admin.ModelAdmin):#Модель пользователей в Админке
    list_display = ('id','username','first_name','last_name','get_html_photo','email','is_staff','is_active','phone_number','date_joined')
    list_display_links = ('username', 'first_name')
    search_fields = ('username', 'first_name','phone_number')
    search_help_text = ('Поиск по пользователям')
    list_editable = ('is_active','is_staff')
    list_filter = ('is_staff', 'is_active',)
    def get_html_photo(self, object):
        if object.user_avatar:
            return mark_safe(f"<img src='{object.user_avatar.url}' width=35>")
    get_html_photo.short_description = 'Фото'
admin.site.register(BuyerUser,BuyerUserAdmin)


class EmployeeInline(admin.TabularInline):#Горизонтальный встроенный редактор модели Сотрудника
    model = Employee
    classes = ('collapse',)
    extra = 1

class JobTitleAdmin(admin.ModelAdmin):#Класс должности в Админке
    list_display = ('id','nameJobTitle', 'slug',)
    list_display_links = ('nameJobTitle', 'slug')
    prepopulated_fields = {'slug': ('nameJobTitle',)}
    inlines = (EmployeeInline,)
admin.site.register(JobTitle, JobTitleAdmin)


class EmployeeAdmin(admin.ModelAdmin):#Класс сотрудники
    list_display = ('id','name', 'slug','second_name','thirt_name','phone_number','get_html_photo','JobTitle',)
    list_display_links = ('name', 'slug','second_name',)
    search_fields = ('name', 'second_name','thirt_name')
    search_help_text = ('Поиск по сотрудникам')
    list_filter = ('JobTitle',)
    prepopulated_fields = {'slug': ('name','second_name','thirt_name')}
    def get_html_photo(self, object):
        if object.employee_avatar:
            return mark_safe(f"<img src='{object.employee_avatar.url}' width=35>")
    get_html_photo.short_description = 'Фото'
admin.site.register(Employee, EmployeeAdmin)


admin.site.site_title = 'Панель администратора сайта'
admin.site.site_header = 'Панель администратора сайта'