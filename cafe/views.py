from django.shortcuts import render, redirect
from .forms import ReservationForm
from django.contrib import messages
from django_app.utils import sms_verification

# Create your views here.


def reserve_table(request):
    form = ReservationForm(request.POST)
    if form.is_valid():
        form.save()
        phone_number = form.cleaned_data['phone']
        name = form.cleaned_data['name']
        num_guests = form.cleaned_data['num_guests']
        sms_verification(client_number=phone_number, client_name=name, number_of_guests=num_guests)
        return redirect('reserve')

    return render(request, 'index.html', {'form': form})