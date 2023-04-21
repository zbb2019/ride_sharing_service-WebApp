from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Driver
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
        # 3. driver page
        return render(request, 'rider/driver.html', {'driver': driver})

# 6. ride details
# 7. sharer page ("join a ride")
# 8. logout (no views needed)
