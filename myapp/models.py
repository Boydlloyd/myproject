from django.db import models
from datetime import datetime,date

# Create your models here.

class Operating_system(models.Model):
    operating_system = models.CharField(max_length=30,unique=True)

    def __str__(self):
        return self.operating_system


class Computer(models.Model):
    computer_name = models.CharField("Computer Name",max_length=30,unique=True)
    IP_address = models.CharField("IP Address",max_length=30)
    MAC_address = models.CharField("MAC Address",max_length=30)
    operating_system = models.ForeignKey(Operating_system,on_delete=models.CASCADE)
    users_name = models.CharField("User",max_length=30)
    location = models.CharField("Location",max_length=30)
    purchase_date=models.DateField("Purchase Date(mm/dd/yyyy)",auto_now_add=False, auto_now=False, blank=False)
    timestamp = models.DateField(auto_now_add=True, auto_now=False, blank=True)
    export_to_CSV=models.BooleanField(default=False)

    def __str__(self):
        return self.computer_name


class ComputerHistory(models.Model):
    computer_name = models.CharField(max_length=30)
    IP_address = models.CharField(max_length=30)
    MAC_address = models.CharField(max_length=30)
    operating_system = models.ForeignKey(Operating_system,on_delete=models.CASCADE)
    users_name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    purchase_date = models.DateField(auto_now_add=False, auto_now=False, blank=True,null=True)
    timestamp = models.DateField(auto_now_add=True, auto_now=False, blank=True, null=True)
    export_to_CSV = models.BooleanField(default=False)
