from django import forms
from .models import *
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from django.forms import  inlineformset_factory
from captcha.fields import CaptchaField


#Форма - регистрация пользователя + капча

class RegisterUserForm(forms.ModelForm):
    #поля ввода формы
    username = forms.CharField(label='Логин', widget=forms.TextInput({'class':'form-control'}))
    password1 = forms.CharField(label='Пароль',help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label='Подтверждение пароля')
    email = forms.EmailField(required=True, label='Ваш e-mail')
    user_avatar = forms.ImageField(required=True,label='Аватарка')
    capcha = CaptchaField(label='Картинка')

    def clean_password(self):#Валидация пароля 1
        password1 = self.cleaned_data["password1"]
        if password1:
            password_validation.validate_password(password1)
        return password1

    def clean(self):#Очистить форму если пароли не совпадают
        super().clean()
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]
        if password1 and password2 and password1 != password2:
            errors = {'password2':ValidationError('Введеные пароли не совпадают', code='password_mismatch')}
            raise ValidationError(errors)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_active = True
        user.is_activated = True
        if commit:
            user.save()
            return user
    class Meta:
        model = BuyerUser
        fields = ('username','first_name','last_name','phone_number','email','password1','password2','user_avatar','capcha')


class ChangeUserInfoForm(forms.ModelForm):
    class Meta:
        model = BuyerUser
        fields = ('username','first_name','last_name','phone_number','email','user_avatar')