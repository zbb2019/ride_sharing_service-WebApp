from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Order(models.Model):  # Order = ride request
    STATUS_CHOICES = (
        ('O', 'Open'),
        ('C', 'Confirmed'),
        ('P', 'Completed'),
    )
    status = models.CharField(
        max_length=2, choices=STATUS_CHOICES, default='O')

    # 1. owner creates an order
    sharableTF = models.BooleanField()
    ownerID = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='ownerID')
    # orderID = id
    destAddr = models.TextField()
    reqArrvDateTime = models.DateTimeField()
    ownerPartySize = models.PositiveIntegerField(default=1)
    # -- optional fields:
    vehicleType = models.CharField(max_length=100, blank=True)
    specialRequest = models.TextField(blank=True)

    # 2. driver & sharer join (opt. when created) -- only 2 NULL=TRUE
    driverID = models.ForeignKey(
        'Driver', blank=True, on_delete=models.SET_NULL, null=True)
    sharerID = models.ForeignKey(
        User, blank=True, on_delete=models.SET_NULL, related_name='sharerID', null=True)
    sharerPartySize = models.PositiveIntegerField(blank=True, default=1)

    def __str__(self):
        return 'order #' + str(self.id)


class Driver(models.Model):
    # driverID = id
    userID = models.OneToOneField(User, on_delete=models.CASCADE)
    vehicleType = models.CharField(max_length=100)
    licensePlateNumber = models.CharField(max_length=10)
    seatCapacity = models.PositiveIntegerField()

    # optional fields:
    specialVehicleInfo = models.TextField(blank=True)

    def __str__(self):
        return 'driver# ' + str(self.userID.username)
