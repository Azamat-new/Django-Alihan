from django import forms
from .models import Car, CarDetails


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['name', 'year', 'price', 'photo_car']


