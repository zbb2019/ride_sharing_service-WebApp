from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Order(models.Model):  # Order = ride request
    status = models.CharField(max_length=100)
    ownerID = models.ForeignKey(User, on_delete=models.CASCADE)
    # orderID = id
    sharableTF = models.BooleanField()
    destAddr = models.TextField()
    reqArrvTime = models.CharField(max_length=100)
    ownerPartySize = models.PositiveIntegerField()
    vehicleType = models.CharField(max_length=100, blank=True)
    specialRequest = models.TextField(blank=True)

    def __str__(self):
        return 'order #' + str(self.id)
