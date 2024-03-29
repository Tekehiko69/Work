# Generated by Django 3.2.4 on 2021-06-10 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry', models.DateField(verbose_name='Дата въезда')),
                ('departure', models.DateField(verbose_name='Дата выезда')),
                ('room', models.CharField(choices=[('Одноместная комната', 'Одноместная комната'), ('Двухместная комната', 'Двухместная комната'), ('Полулюкс', 'Полулюкс'), ('Люкс', 'Люкс')], max_length=19, verbose_name='Выберите компнату')),
                ('email', models.EmailField(max_length=254, verbose_name='Введите почтовый адрес')),
                ('name', models.CharField(max_length=15, verbose_name='Введите ваше имя')),
            ],
            options={
                'verbose_name': 'Бронь номера',
                'verbose_name_plural': 'Бронирование номера',
            },
        ),
    ]
