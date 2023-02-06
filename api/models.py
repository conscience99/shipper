from django.db import models


class Package(models.Model):
    pid=models.CharField(max_length=250, blank=True, null=True)
    tracking=models.CharField(max_length=250, blank=True, null=True)
    sender=models.CharField(max_length=250, blank=True, null=True)
    weight=models.CharField(max_length=250, blank=True,null=True)
    description=models.CharField(max_length=250,blank=True,null=True)
    reciever=models.CharField(max_length=250, blank=True, null=True)
    departure=models.CharField(max_length=250, blank=True, null=True)
    arival=models.CharField(max_length=250, blank=True, null=True)
    destination_address = models.CharField(max_length=250, blank=True, null=True)
    date_sent=models.DateField(blank=True, null=True)
    est=models.DateField(blank=True, null=True)
    status_name=models.CharField(max_length=250, blank=True, null=True)
    status_note=models.TextField(blank=True, null=True)
    status_date=models.DateField(blank=True, null=True)
    is_confirmed=models.BooleanField(default=False)
    is_picked=models.BooleanField(default=False)
    is_departed=models.BooleanField(default=False)
    is_dispachted=models.BooleanField(default=False)
    is_delivered=models.BooleanField(default=False)

    




