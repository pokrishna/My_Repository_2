from django.db import models

# Create your models here.
class logintable(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    usertype=models.CharField(max_length=30)

class homeDevices(models.Model):
    device_name=models.CharField(max_length=30)
    device_desc=models.CharField(max_length=30)
    device_status=models.CharField(max_length=30)