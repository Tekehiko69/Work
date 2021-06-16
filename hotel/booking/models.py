from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Booking(models.Model):
    userss = models.ForeignKey(User,null=True, on_delete=models.CASCADE, verbose_name='Кто забронировал', default=None)
    entry = models.DateField('Дата въезда')
    departure = models.DateField('Дата выезда')
    choice_room = (
        ('Одноместная комната','Одноместная комната'),
        ('Двухместная комната','Двухместная комната'),
        ('Полулюкс', 'Полулюкс'),
        ('Люкс', 'Люкс'),
    )

    room = models.CharField('Выберите компнату', max_length=19, choices=choice_room)

    email = models.EmailField('Введите почтовый адрес')

    name = models.CharField('Введите ваше имя', max_length=15)


    def __str__(self):
        return self.room

    def get_absolute_url(self):
        return f'/{self.id}'


    class Meta:
        verbose_name = 'Бронь номера'
        verbose_name_plural = 'Бронирование номера'