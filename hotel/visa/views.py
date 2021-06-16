from django.shortcuts import render, redirect
from .forms import VisaForm
from .models import Visa

# Create your views here.
def visa(request):
    if request.method == 'POST':
        form = VisaForm(request.POST)
        if form.is_valid():
            instance = form.save()
            instance.users = request.user
            instance.save()
            return redirect('main-page')
    form = VisaForm

    data = {
        'form': form,
    }

    return render(request, 'visa/visa.html', data)


def VisaShow(request):
    sho = Visa.objects.filter(users=request.user)
    return render(request, 'visa/my_visa_status.html', {'sho': sho})