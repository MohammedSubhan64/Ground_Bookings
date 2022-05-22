from django.db import models
import datetime
# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    des=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name

class Bookings(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    number =models.CharField(max_length=10,default='phone number')
    date = models.CharField(max_length=120)
    time = models.CharField(max_length=120)
    groundtype = models.CharField(max_length=120)
    selectground = models.CharField(max_length=120)

    
    def __str__(self):
        return self.name

class CricketTiming(models.Model):
    newdate =models.DateTimeField("newdate",null=True, blank=True)
    c1_t1 =models.CharField(max_length=20)
    c1_t2 =models.CharField(max_length=20)
    c1_t3 =models.CharField(max_length=20)
    c2_t1 =models.CharField(max_length=20)
    c2_t2 =models.CharField(max_length=20)
    c2_t3=models.CharField(max_length=20)
    c3_t1=models.CharField(max_length=20)
    c3_t2=models.CharField(max_length=20)
    c3_t3=models.CharField(max_length=20)
    c4_t1=models.CharField(max_length=20)
    c4_t2=models.CharField(max_length=20)
    c4_t3=models.CharField(max_length=20)


