from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.info_book, name='book'),
    path('film/', views.cinema, name='film'),
    path('car/', views.car_view, name='car'),
    path('car/<int:car_id>/', views.car_detail, name='details'),
    path('add-car/', views.add_car, name='add_car'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

