from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Visa(models.Model):
    users = models.ForeignKey(User, null=True, on_delete=models.CASCADE, verbose_name='Кто отправил заявку', default=None)
    entry =  models.DateField('Дата въезда')
    departure = models.DateField('Дата выезда')
    guests = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
    )
    guest = models.CharField('Количество людей', max_length=1, choices=guests)
    email = models.EmailField('Введите почтовый адрес')
    citizenship = models.CharField('Гражданство', max_length=25)
    city_of_visit = models.CharField('Город посещения', max_length=50)
    hotel = models.CharField('Отель', max_length=30)
    goal_of_visit = models.CharField('Цель поездки', max_length=200)

    def __str__(self):
        return self.city_of_visit

    def get_absolute_url(self):
        return f'/{self.id}'

    class Meta:
        verbose_name = 'Визовая поддержка'
        verbose_name_plural = 'Визовая поддержка'
