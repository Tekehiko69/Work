from .models import Booking
from django.forms import ModelForm, Select, TextInput, DateInput, EmailInput


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['entry', 'departure', 'room', 'email', 'name']
        choice_room = [
            ('Одноместная комната', 'Одноместная комната'),
            ('Двухместная комната', 'Двухместная комната'),
            ('Полулюкс', 'Полулюкс'),
            ('Люкс', 'Люкс'),
        ]

        widgets = {
            'entry' : DateInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Дата въезда',
            }),
            'departure' : DateInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Дата выезда',
            }),
            'room' : Select(choices=choice_room, attrs={
                'class' : 'form-control',
                'placeholder' : 'Выберите номер',
            }),
            'email' : EmailInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Почтовый адрес',
            }),
            'name' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Ваше имя',
            }),
        }