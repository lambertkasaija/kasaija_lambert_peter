from django.shortcuts import render,redirect
from .models import FlightPassenger
from .forms import FlightPassengerForm
from django.contrib import messages


# Create your views here.
def add_booking(request):
    if request.method == 'POST':
        form = FlightPassengerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submitted successfully!')
            return redirect('/')
        else:
            messages.error(request, 'There was an error with your submission.')
    else:
        form = FlightPassengerForm()

    return render(request, 'booking/add_booking.html', {'form':form})