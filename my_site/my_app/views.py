from django.shortcuts import render, get_object_or_404
from .models import Book, Cinematica, Car, CarDetails


def info_book(request):
    book = Book.objects.all()
    return render(request, 'my_app/index.html', {'book': book})


def cinema(request):
    film = Cinematica.objects.all()
    return render(request, 'my_app/index.html', {'film': film})


def car_view(request):
    auto = Car.objects.all()
    return render(request,
                  'my_app/car.html',
                  {"auto": auto})


# def car_detail(request):
#     auto_detail = CarDetails.objects.all()
#     return render(request,
#                   'my_app/details.html',
#                   {"auto_detail": auto_detail})

def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    details = CarDetails.objects.filter(details=car).first()
    return render(request,
                  'my_app/details.html',
                  {"car": car, "details": details})

