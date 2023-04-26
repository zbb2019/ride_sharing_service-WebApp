from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Driver, Order
from .forms import DriverRegistrationForm, OwnerOrderForm, SharerSearchForm
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
                request, f'Account created for {username}! Redirect to Login page.')
            return redirect('rider-home')
        messages.warning(request, f'Account creation failed!')
    else:
        form = UserCreationForm()
    return render(request, 'rider/create_account.html', {'form': form})


@login_required
def home(request):
    # 5. main user page after login ("Ride")
    if request.method == 'POST':
        form = OwnerOrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.ownerID = request.user
            order.totalPartySize = order.ownerPartySize
            order.save()
            messages.success(
                request, f'Order requested successfully!')
            return redirect('rider-home')
        messages.warning(
            request, f'Order request failed!')
    else:
        form = OwnerOrderForm()
    rides = Order.objects.filter(
        ownerID=request.user) | Order.objects.filter(sharerID=request.user)
    open_rides = rides.filter(status='O')
    confirmed_rides = rides.filter(status='C')
    return render(request, 'rider/home.html', {'form': form, 'open_rides': open_rides, 'confirmed_rides': confirmed_rides})


@login_required
def driver(request):
    # 3. driver registration
    driver = Driver.objects.filter(userID=request.user).first()
    if not driver:
        if request.method == 'POST':
            form = DriverRegistrationForm(request.POST)
            if form.is_valid():
                driver = form.save(commit=False)
                driver.userID = request.user
                driver.save()
                return redirect('rider-driver')
        form = DriverRegistrationForm()
        return render(request, 'rider/driver_registration.html', {'form': form})
    else:
        # 4. driver page
        def getOpenRides(user):
            # filter open rides for the driver
            d = Driver.objects.get(userID=user)
            open_rides = Order.objects.filter(
                status='O', totalPartySize__lte=d.seatCapacity)
            # filter rides that have the same vihicle type or no vehicle type
            open_rides = open_rides.filter(
                vehicleType=d.vehicleType) | open_rides.filter(vehicleType='')
            # filter rides that have the same special info or no special info
            open_rides = open_rides.filter(
                specialRequest=d.specialVehicleInfo) | open_rides.filter(specialRequest='')
            return open_rides

        def getOnGoingRides(user):
            d = Driver.objects.get(userID=user)
            # filter on-going rides for the driver
            on_going_rides = Order.objects.filter(status='C', driverID=d)
            return on_going_rides

        if request.method == 'GET':
            # if the driver clicked 'search for rides' (by filtering urls)
            if request.GET.get('showresults', None):
                open_rides = getOpenRides(request.user)
            else:
                open_rides = None
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
            if request.GET.get('showresults', None):
                return redirect('/driver/?showresults=true')
        ongoing_rides = getOnGoingRides(request.user)
        return render(request, 'rider/driver.html', {'driver': driver, 'ongoing_rides': ongoing_rides})


@login_required
def ride_details(request):
    # 6. ride details
    if request.method == 'GET':
        rideid = request.GET.get('rideid', None)
        ride = Order.objects.get(id=rideid) if rideid else None
        if not ride:
            return redirect('rider-home')
        role = None
        if ride.driverID == request.user:
            role = 'driver'
        elif ride.ownerID == request.user:
            role = 'owner'
        elif ride.sharerID == request.user:
            role = 'sharer'
        return render(request, 'rider/ride_details.html', {'ride': ride, 'role': role})


@login_required
def sharer(request):
    # 7. sharer page ("join a ride")
    if request.method == 'POST':
        form = SharerSearchForm(request.POST)
        if form.is_valid():
            # filter open rides
            open_rides = Order.objects.filter(
                status='O', sharableTF=True, sharerID=None)
            # filter destination
            open_rides = open_rides.filter(
                destAddr=form.cleaned_data['destAddr'])
            # filter datetime range
            open_rides = open_rides.filter(reqArrvDateTime__range=(
                form.cleaned_data['reqArrvDateTimeEarly'], form.cleaned_data['reqArrvDateTimeLate']))
            party_size = form.cleaned_data['sharerPartySize']
            return render(request, 'rider/sharer.html', {'form': form, 'open_rides': open_rides, 'party_size': party_size})
        else:
            # joining a ride
            ride_id = request.POST.get('ride_id', None)
            party_size = request.POST.get('party_size', None)
            if ride_id and party_size:
                ride = Order.objects.get(id=ride_id)
                ride.totalPartySize += int(party_size)
                ride.sharerPartySize = int(party_size)
                ride.sharerID = request.user
                ride.save()
                return redirect('rider-sharer')
        return redirect('rider-sharer')
    form = SharerSearchForm()
    return render(request, 'rider/sharer.html', {'form': form})

# 8. logout (no views needed)
