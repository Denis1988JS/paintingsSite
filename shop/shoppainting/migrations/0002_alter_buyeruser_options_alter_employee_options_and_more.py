# Generated by Django 4.2.2 on 2023-07-19 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoppainting', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='buyeruser',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name': 'Сотрудник', 'verbose_name_plural': 'Сотрудники'},
        ),
        migrations.AlterModelOptions(
            name='jobtitle',
            options={'verbose_name': 'Должность', 'verbose_name_plural': 'Должности'},
        ),
    ]
