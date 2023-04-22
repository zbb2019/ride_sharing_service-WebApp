from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Driver, Order
from .forms import DriverRegistrationForm
# Create your views here.

# 1. login (no views needed)


def create_account(request):
    # 2. create an account
    # user resgistration using django auth
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # display message
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Account created for {username}! Redirect to home page.')
            return redirect('/home/')

    else:
        form = UserCreationForm()
    return render(request, 'rider/create_account.html', {'form': form})


@login_required
def home(request):
    # 5. main user page after login ("Ride")
    return render(request, 'rider/home.html')


@login_required
def driver(request):
    # 4. driver registration
    driver = Driver.objects.filter(userID=request.user).first()
    if not driver:
        if request.method == 'POST':
            form = DriverRegistrationForm(request.POST)
            if form.is_valid():
                driver = form.save(commit=False)
                driver.userID = request.user
                driver.save()
                return redirect('/driver/')
        form = DriverRegistrationForm()
        return render(request, 'rider/driver_registration.html', {'form': form})
    else:
        def getOpenRides(user):
            # filter open rides for the driver
            d = Driver.objects.get(userID=user)
            open_rides = Order.objects.filter(status='O', totalPartySize__lte=d.seatCapacity)
            # filter rides that have the same vihicle type or no vehicle type
            open_rides = open_rides.filter(vehicleType=d.vehicleType) | open_rides.filter(vehicleType='')
            # filter rides that have the same special info or no special info
            open_rides = open_rides.filter(specialRequest=d.specialVehicleInfo) | open_rides.filter(specialRequest='')
            return open_rides
        def getOnGoingRides(user):
            d = Driver.objects.get(userID=user)
            # filter on-going rides for the driver
            on_going_rides = Order.objects.filter(status='C', driverID=d)
            return on_going_rides
        if request.method == 'GET':
            # if query string has 'open_rides' then filter open rides
            open_rides = getOpenRides(request.user) if request.GET.get('open_rides', None) else None
            ongoing_rides = getOnGoingRides(request.user)
            return render(request, 'rider/driver.html', {
                'driver': driver,
                'open_rides': open_rides,
                'ongoing_rides': ongoing_rides}
            )
        if request.method == 'POST':
            # if the driver accepts a ride
            if request.POST.get('accept_ride', None):
                ride_id = request.POST.get('accept_ride')
                ride = Order.objects.get(id=ride_id)
                ride.driverID = driver
                ride.status = 'C'
                ride.save()
            if request.POST.get('finish_ride', None):
                ride_id = request.POST.get('finish_ride')
                ride = Order.objects.get(id=ride_id)
                ride.status = 'P'
                ride.save()
            return redirect('/driver/?open_rides=true')
        # 3. driver page
        return render(request, 'rider/driver.html', {'driver': driver})

# 6. ride details
# 7. sharer page ("join a ride")
# 8. logout (no views needed)
