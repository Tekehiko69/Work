from django.contrib.auth.models import User
from django import forms
from django.db import models

class LoginForms(forms.Form):
    username= forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль',widget=(forms.PasswordInput))


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Логин', )
    password = forms.CharField(label='Пароль', widget= forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget= forms.PasswordInput)


    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')


    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают!')
        return cd['password2']



