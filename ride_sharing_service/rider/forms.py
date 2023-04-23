from django import forms
from .models import Driver, Order


class DriverRegistrationForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ('vehicleType', 'licensePlateNumber',
                  'seatCapacity', 'specialVehicleInfo')
        labels = {
            'vehicleType': 'Vehicle Type',
            'licensePlateNumber': 'License Plate Number',
            'seatCapacity': 'Seat Capacity',
            'specialVehicleInfo': 'Any Special Vehicle Info (optional)'
        }


class OwnerOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('sharableTF', 'destAddr', 'reqArrvDateTime',
                  'ownerPartySize', 'vehicleType', 'specialRequest')
        labels = {'sharableTF': 'Sharable or Not',
                  'destAddr': 'Destination Address',
                  'reqArrvDateTime': 'Requested Arrival Date and Time(yyyy-mm-dd hh:mm:ss)',
                  'ownerPartySize': 'Your Party Size',
                  'vehicleType': 'Vehicle Type',
                  'specialRequest': 'Any Special Requests (optional)'}


class SharerSearchForm(forms.Form):
    destAddr = forms.CharField(label='Destination Address')
    reqArrvDateTimeEarly = forms.DateTimeField(label='Earliest Requested Arrival Date and Time(yyyy-mm-dd hh:mm:ss)')
    reqArrvDateTimeLate = forms.DateTimeField(label='Latest Requested Arrival Date and Time(yyyy-mm-dd hh:mm:ss)')
