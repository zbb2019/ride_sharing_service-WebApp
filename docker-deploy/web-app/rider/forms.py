from django import forms
from django.utils.safestring import mark_safe
from .models import Driver, Order


class DriverRegistrationForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ('name', 'vehicleType', 'licensePlateNumber',
                  'seatCapacity', 'specialVehicleInfo')
        labels = {
            'name': 'Your Name',
            'vehicleType': 'Vehicle Type',
            'licensePlateNumber': 'License Plate Number',
            'seatCapacity': mark_safe('Seat Capacity<br><small>(must be >= 1)</small>'),
            'specialVehicleInfo': 'Any Special Vehicle Info (optional)'
        }


class OwnerOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('sharableTF', 'destAddr', 'reqArrvDateTime',
                  'ownerPartySize', 'vehicleType', 'specialRequest')
        labels = {'sharableTF': 'Sharable or Not',
                  'destAddr': 'Destination Address',
                  'reqArrvDateTime': mark_safe('Requested Arrival Date and Time<br><small>(e.g., yyyy-mm-dd hh:mm:ss)</small>'),
                  'ownerPartySize': 'Your Party Size',
                  'vehicleType': 'Vehicle Type (optional)',
                  'specialRequest': 'Any Special Requests (optional)'}


class SharerSearchForm(forms.Form):
    destAddr = forms.CharField(label='Destination Address')
    reqArrvDateTimeEarly = forms.DateTimeField(
        label=mark_safe('Earliest Requested Arrival Date and Time<br><small>(e.g., yyyy-mm-dd hh:mm:ss)</small>'))
    reqArrvDateTimeLate = forms.DateTimeField(
        label=mark_safe('Latest Requested Arrival Date and Time<br><small>(e.g., yyyy-mm-dd hh:mm:ss)</small>'))
    sharerPartySize = forms.IntegerField(
        label='Sharer Party Size', min_value=1)
