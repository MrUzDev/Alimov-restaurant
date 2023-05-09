from django.db import models
from django.db import models


class Reservation(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True, null=True)
    date = models.DateField()
    time = models.TimeField()
    num_guests = models.PositiveIntegerField()
    created_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Бронирование'

    def __str__(self):
        return str(self.name)


class Menu(models.Model):
    CATEGORY_CHOICES = [
        ('foods', 'Foods'),
        ('drinks', 'Drinks'),
    ]
    image = models.ImageField(upload_to='menu_images', blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    price = models.CharField(max_length=15, blank=True, null=True)
    category = models.CharField(max_length=55, choices=CATEGORY_CHOICES)
    created_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Меню'

    def __str__(self):
        return str(self.title)


class Contact(models.Model):
    location = models.CharField(max_length=555, blank=True, null=True)
    phone_number = models.CharField(max_length=55)
    email = models.CharField(max_length=55, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return str(self.phone_number)


class MenuGallery(models.Model):
    images = models.ImageField(upload_to='menu_images')
    created_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Галерея'

    def __str__(self):
        return str(self.created_date)


class AboutUs(models.Model):
    image = models.ImageField(upload_to='menu_images')
    body = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'О нас'

    def __str__(self):
        return str(self.created_date)
