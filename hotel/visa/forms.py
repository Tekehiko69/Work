from .models import Visa
from django.forms import ModelForm, TextInput, Textarea, Select,  DateInput, EmailInput

class VisaForm(ModelForm):
    class Meta:
        model = Visa
        fields = ['entry', 'departure', 'guest', 'email', 'citizenship', 'city_of_visit', 'hotel', 'goal_of_visit']
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

        widgets= {
            'entry': DateInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Дата въезда',
            }),
            'departure': DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата выезда',
            }),'guest': Select(attrs={
                'class' : 'form-control',
                'placeholder' : 'Количество гостей',
            }),'email': EmailInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Почта',
            }),'citizenship': TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Гражданство',
            }),
            'city_of_visit': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Город посещения',
            }),
            'hotel': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Отель',
            }),
            'goal_of_visit': Textarea(attrs={
                'class' : 'form-control',
                'placeholder' : 'Цель визита',
            }),

        }