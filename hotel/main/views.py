from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def gallery(request):
    return render(request, 'main/gallery.html')

def restaurant(request):
    return render(request, 'main/restaurant.html')

def contact(request):
    return render(request, 'main/contact.html')

def room(request):
    return render(request, 'main/room.html')

def service(request):
    return render(request, 'main/service.html')

def en(request):
    return render(request, 'main/en_index.html')