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
                  'reqArrvDateTime': 'Requested Arrival Date and Time',
                  'ownerPartySize': 'Your Party Size',
                  'vehicleType': 'Vehicle Type',
                  'specialRequest': 'Any Special Requests (optional)'}


class SharerSearchForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('destAddr', 'reqArrvDateTime', 'reqArrvDateTime',
                  'ownerPartySize')
        labels = {'destAddr': 'Destination Address',
                  'reqArrvDateTime': 'Earliest Required Arrival Date and Time',
                  'reqArrvDateTime': 'Latest Required Arrival Date and Time',
                  'ownerPartySize': 'Your Party Size'}
