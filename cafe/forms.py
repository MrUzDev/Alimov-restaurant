from django import forms
from django.forms.widgets import DateTimeInput
from cafe.models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'phone', 'date', 'time', 'num_guests']
        # widgets = {
        #     'date_time': DateTimeInput(attrs={'type': 'datetime-local'})
        # }
