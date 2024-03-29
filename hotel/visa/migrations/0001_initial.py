# Generated by Django 3.2.4 on 2021-06-14 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry', models.DateField(verbose_name='Дата въезда')),
                ('departure', models.DateField(verbose_name='Дата выезда')),
                ('guest', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9')], max_length=1, verbose_name='Количество людей')),
                ('email', models.EmailField(max_length=254, verbose_name='Введите почтовый адрес')),
                ('citizenship', models.CharField(max_length=25, verbose_name='Гражданство')),
                ('city_of_visit', models.CharField(max_length=50, verbose_name='Город посещения')),
                ('hotel', models.CharField(max_length=30, verbose_name='Отель')),
                ('goal_of_visit', models.CharField(max_length=200, verbose_name='Цель поездки')),
            ],
            options={
                'verbose_name': 'Визовая поддержка',
                'verbose_name_plural': 'Визовая поддержка',
            },
        ),
    ]
