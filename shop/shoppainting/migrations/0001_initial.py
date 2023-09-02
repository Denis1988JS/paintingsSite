# Generated by Django 4.2.2 on 2023-07-10 16:40

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields
import shoppainting.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountryPainting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_country', models.CharField(max_length=50, verbose_name='Страна')),
                ('slug', models.SlugField(unique=True, verbose_name='URL-country')),
            ],
            options={
                'verbose_name': 'Страна',
                'verbose_name_plural': 'Страны',
            },
        ),
        migrations.CreateModel(
            name='FormatPainting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('canvas', models.CharField(max_length=50, unique=True, verbose_name='Материал')),
                ('size', models.CharField(error_messages={'invalid': 'Введите в формате 00x00 или 000x000'}, help_text='Размер в формате 00x00 или 000x000', max_length=15, validators=[shoppainting.models.ValidateFormatPaintingSize], verbose_name='Размер')),
            ],
            options={
                'verbose_name': 'Характеристика картины',
                'verbose_name_plural': 'Характеристики картин',
            },
        ),
        migrations.CreateModel(
            name='JobTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameJobTitle', models.CharField(max_length=50, verbose_name='Должность')),
                ('slug', models.SlugField(verbose_name='URL-по должностям')),
            ],
        ),
        migrations.CreateModel(
            name='Painting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75, verbose_name='Название')),
                ('slug', models.SlugField(max_length=75, verbose_name='URL-картины')),
                ('autor', models.CharField(max_length=75, verbose_name='Автор')),
                ('year', models.IntegerField(verbose_name='Год')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('avaliable', models.BooleanField(db_index=True, default=True, verbose_name='Наличие')),
                ('imagePainting', models.ImageField(upload_to='photos/painting/%Y/%m/%d/', verbose_name='Фото картины')),
                ('countryPaint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoppainting.countrypainting', verbose_name='Страна картины')),
                ('formPaint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoppainting.formatpainting', verbose_name='Формат картины')),
            ],
            options={
                'verbose_name': 'Картина',
                'verbose_name_plural': 'Картины',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя сотрудника')),
                ('slug', models.SlugField(max_length=30, verbose_name='URL-сотрудника')),
                ('second_name', models.CharField(max_length=30, verbose_name='Фамилия сотрудника')),
                ('thirt_name', models.CharField(max_length=30, verbose_name='Отчество сотрудника')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True, verbose_name='Номер телефона')),
                ('employee_avatar', models.ImageField(upload_to='photos/employee/%Y/%m/%d/', verbose_name='Аватарка сотрудника')),
                ('employee_content', models.TextField(max_length=5000, verbose_name='О сотруднике')),
                ('JobTitle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='JobTitle', to='shoppainting.jobtitle')),
            ],
        ),
        migrations.CreateModel(
            name='BuyerUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='Активный пользователь')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True, verbose_name='Номер телефона')),
                ('user_avatar', models.ImageField(upload_to='photos/users_avatar/%Y/%m/%d/', verbose_name='Аватарка пользователя')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]