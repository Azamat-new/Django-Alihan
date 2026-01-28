from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField()
    price = models.IntegerField()


class Gallery(models.Model):
    title = models.CharField(max_length=15)
    photo = models.ImageField()
    date = models.DateTimeField()


class Cinematica(models.Model):
    title = models.CharField(max_length=20)
    age_category = models.PositiveSmallIntegerField()
    cinema_photo = models.ImageField()

    def __str__(self):
        return self.title


class Car(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField()
    price = models.IntegerField()
    photo_car = models.ImageField()

    def __str__(self):
        return self.name


class CarDetails(models.Model):
    details = models.ForeignKey(Car, on_delete=models.CASCADE)
    description = models.TextField(max_length=700)
    country = models.CharField(max_length=50)
    photo_car_detail = models.ImageField()
    is_stock = models.BooleanField(default=True)


