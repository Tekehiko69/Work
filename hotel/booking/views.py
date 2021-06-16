from django.shortcuts import render, redirect
from django.views.generic import  DeleteView

from .forms import BookingForm
from .models import Booking as boo
from django.contrib import auth

# Create your views here.
def booking(request):
    error = ''
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            instance = form.save()
            instance.userss =request.user
            instance.save()
            return redirect('main-page')
        else:
            error = 'Ошибка ввода'

    form = BookingForm

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'booking/booking.html', data)


def BookingShow(request):
    show = boo.objects.filter(userss=request.user)
    return render(request, 'account/my_booking.html', {'show': show})








