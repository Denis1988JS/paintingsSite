import json
import simplejson
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView
from django.shortcuts import get_object_or_404


from .forms import RegisterUserForm, ChangeUserInfoForm
from .models import *
from .utils import DataMixin



# Create your views here.

# def index(request):#Главная страница - через функцию
#     title = 'Главная страница'
#     data = {'title':title,'content':content}
#     return render(request, 'shoppainting/index.html', context=data)

class MainPage(ListView,DataMixin):#Главная страница - через класс - там же FETCH запрос
    model = CountryPainting
    context_object_name = 'CountryPainting'
    template_name = 'shoppainting/index.html'
    def post(self,request):
        if request.method == 'POST':
            data = json.loads(request.body)
            filterCountry = CountryPainting.objects.get(name_country=data['country'])
            filterPaintings = filterCountry.painting_set.filter(avaliable = True).values('id','name', 'slug','autor','imagePainting','price',
                                                                                         'formPaint_id','countryPaint',)
            def takeFormPainting():#Получение строки - формат картины!!!
                for item in filterPaintings:
                    for values in item:
                        if values=='formPaint_id':
                            fP = FormatPainting.objects.get(id=item[values])
                            item[values]=fP.__str__()
                            print(values,item[values], fP,type(fP.__str__()))
            takeFormPainting()
            filterPaintings = list(filterPaintings)
            filterPaintings = simplejson.dumps(filterPaintings,use_decimal=True)
            return JsonResponse(filterPaintings,safe=False)
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['artist'] = Employee.objects.filter(JobTitle__id=1)
        context['countryFrance'] = context['CountryPainting'][0]
        context['countyList'] = CountryPainting.objects.all()
        context['paintings'] = context['CountryPainting'][0].painting_set.filter(avaliable = True)
        c_def = self.get_user_context()
        context = dict(list(context.items()) + list(c_def.items()))
        return context
#Страница о нас
def aboutUs(request):
    title = 'О нас'
    france = CountryPainting.objects.get(id=1)
    data = {'title':title,'france':france}
    return render(request, 'shoppainting/about.html', context=data)

#Страница Новинки - последние 10 картин
class NewPaintings(ListView,DataMixin):
    model = Painting
    template_name = "shoppainting/newPaintings.html"
    context_object_name = 'newPaintings'
    queryset = Painting.objects.filter(avaliable=True).order_by('id')[10::-1]
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        context = dict(list(context.items()) + list(c_def.items()))
        context["title"] = 'Новинки'
        print(context)
        return context

#Страница - детальное отображение картины
class DetailViewPaintings(DetailView,DataMixin):
    model = Painting
    template_name = 'shoppainting/painting_detail.html'
    slug_url_kwarg = 'painting_slug'
    context_object_name = 'paint'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['artist'] = Employee.objects.filter(JobTitle__id=1)
        context['title'] = context['paint']
        c_def = self.get_user_context()
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#Страница картины по годам
class PaintingsYear(TemplateView,DataMixin):
    model = Painting
    template_name = "shoppainting/paintings_year.html"
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['paintings'] = Painting.objects.filter(year=context["year"],avaliable = True).order_by('countryPaint')
        context["title"] = f'Картины {str((context["year"]))} года'
        c_def = self.get_user_context()
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#Страница сотрудники все
class EmployeesPage(ListView,DataMixin):
    model = Employee
    template_name = "shoppainting/employees.html"
    context_object_name = 'employees'
    queryset = Employee.objects.all().order_by('-JobTitle')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Наша команда'
        c_def = self.get_user_context()
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#Страница художники
class EmployeesPageArtists(ListView,DataMixin):
    model = Employee
    template_name = "shoppainting/artists.html"
    context_object_name = 'artists'
    queryset = Employee.objects.filter(JobTitle__id=1)
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Наши художники'
        c_def = self.get_user_context()
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#Страница менеджеры
class EmployeesPageMenegers(ListView, DataMixin):
    model = Employee
    template_name = "shoppainting/menegers.html"
    context_object_name = 'menegers'
    queryset = Employee.objects.exclude(JobTitle__id=1)
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Наши менеджеры'
        c_def = self.get_user_context()
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#Страница детально сотрудник
class DetailEmployeesPage(DetailView,DataMixin):
    model = Employee
    template_name = 'shoppainting/employee_detail.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'employee'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        context = dict(list(context.items()) + list(c_def.items()))
        context['title'] = context['employee'] 
        return context

#Страница показать картины согласно страны
class PaintingsCountry(TemplateView,DataMixin):
    model = Painting
    template_name = "shoppainting/paintings_country.html"
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['paintings'] = Painting.objects.filter(countryPaint__name_country=context["country"], avaliable=True)
        context["title"] = f'Картины {str((context["country"]))}'
        c_def = self.get_user_context()
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#Страница Продукция - через функцию
def ourProducts(request):
    title = 'Наша продукция'
    products = Painting.objects.filter(avaliable=True).order_by('name')[:100:]
    artist = Employee.objects.filter(JobTitle__id=1)
    countyList = CountryPainting.objects.all()
    france = CountryPainting.objects.get(id=1)
    dataInfo = {'title': title,'products':products,'artist':artist,'countyList':countyList,'france':france}
    return render(request, "shoppainting/ourProducts.html", context=dataInfo)

#Регистрация пользователя + капча
class RegisterUserView(CreateView,DataMixin):
    model = BuyerUser
    template_name = 'shoppainting/register_user.html'
    form_class = RegisterUserForm
    france = CountryPainting.objects.get(id=1)
    success_url = reverse_lazy('home')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = f'Страница регистрации'
        c_def = self.get_user_context()
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#Страница авторизация на сайте
class LoginUser(LoginView,DataMixin):
    template_name = 'shoppainting/login_user.html'
    france = CountryPainting.objects.get(id=1)
    extra_context = {'title': 'Авторизация пользователя','france':france}

#Выход пользователя
class LogoutPage(LoginRequiredMixin,LogoutView):
    template_name = 'shoppainting/logout.html'
    france = CountryPainting.objects.get(id=1)
    countyList = CountryPainting.objects.all()
    extra_context = {'title': 'Авторизация пользователя', 'france': france,'countyList':countyList}

#Личный кабинет пользователя
class UserProfile(LoginRequiredMixin,DetailView,DataMixin):
    model = BuyerUser
    template_name = 'shoppainting/profile_user.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = f'Личный кабинет пользователя'
        c_def = self.get_user_context()
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#Страница редактирования данных пользователя
class ChangeUserInfoView(SuccessMessageMixin,LoginRequiredMixin,UpdateView):
    model = BuyerUser
    template_name = 'shoppainting/change_user_info.html'
    form_class = ChangeUserInfoForm
    success_message = 'Данные успешно изменены'
    france = CountryPainting.objects.get(id=1)
    extra_context = {'france': france}
    success_url = reverse_lazy('home')
    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)
    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset,pk=self.user_id)

#Страница редактирования пароля пользователя
class ChangePasswordUser(SuccessMessageMixin, LoginRequiredMixin,PasswordChangeView):
    template_name = 'shoppainting/change_password.html'
    france = CountryPainting.objects.get(id=1)
    extra_context = {'france': france}
    success_message = 'Пароль успешно изменен'
    success_url = reverse_lazy('home')

#Страница - репродукции
class Reproductions(TemplateView,DataMixin):
    template_name = 'shoppainting/reproductions.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        context = dict(list(context.items()) + list(c_def.items()))
        return context
#Страница - о нас
















