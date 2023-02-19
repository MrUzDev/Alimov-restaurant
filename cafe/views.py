from django.shortcuts import render, redirect
from .forms import ReservationForm
from django.contrib import messages


# Create your views here.


def reserve_table(request):
    form = ReservationForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Your table has been booked.')
        return redirect('reserve')

    return render(request, 'index.html', {'form': form})