from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .forms import  LoginForms , RegistrationForm



# Create your views here.

def user_login(request):
    if request.method == 'POST':
        form = LoginForms(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username = cd['username'], password = cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
                else:
                    return HttpResponse('Аккаунт заблокирован')
            else:
                return HttpResponse('Неверно введен пароль')
    else:
        form = LoginForms()

    return render(request,'account/login.html', {'form' : form})


def user_register(request):
    error = ''
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'main/index.html', {'new_user': new_user})
        else:
            error = 'Ошибка ввода'
    else:
        user_form = RegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})


def logout_user(request):
    logout(request)
    return redirect('login')




