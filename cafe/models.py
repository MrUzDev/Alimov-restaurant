from django.db import models

# Create your models here.

from django.db import models


class Reservation(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True, null=True)
    date = models.DateField()
    time = models.TimeField()
    num_guests = models.PositiveIntegerField()

    def __str__(self):
        return str(self.name)