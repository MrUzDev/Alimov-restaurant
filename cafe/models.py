from django.db import models
from django.db import models


class Reservation(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True, null=True)
    date = models.DateField()
    time = models.TimeField()
    num_guests = models.PositiveIntegerField()
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)


class Menu(models.Model):
    image = models.ImageField(upload_to='menu_images')
    title = models.CharField(max_length=200)
    body = models.TextField()
    price = models.CharField(max_length=15)
    category = models.CharField(max_length=55)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)


class Contact(models.Model):
    location = models.CharField(max_length=555)
    phone_number = models.CharField(max_length=55)
    email = models.CharField(max_length=55, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.phone_number)


class MenuGallery(models.Model):
    images = models.ImageField(upload_to='menu_images')
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.created_date)


class AboutUs(models.Model):
    image = models.ImageField(upload_to='menu_images')
    body = models.TextField()
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.created_date)
