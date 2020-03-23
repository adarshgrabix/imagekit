from django.db import models

# Create your models here.
class data(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    ipaddress = models.CharField(null=True,max_length=100)


class iplist(models.Model):
    ip = models.CharField(max_length=50)
    count = models.IntegerField(blank=True,default=0, null=True)
    idate = models.DateField(blank=True, null=True)

