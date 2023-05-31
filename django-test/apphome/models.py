from django.db import models
from django.contrib.postgres.fields import ArrayField  


class Customers(models.Model):
    cid = models.IntegerField(default=0)
    rid = models.IntegerField(default=0)
    menu = ArrayField(models.IntegerField(default=0), blank=True) #integerarry  
    num_guest = models.IntegerField(default=0)
    enter_time = models.DateTimeField("enter time")
    out_time = models.DateTimeField("out time")
    Total_time = models.DurationField() #interval

class Restaurants(models.Model):
    #rid = models.ForeignKey(Question, on_delete=models.CASCADE)
    rid = models.IntegerField(default=0)
    rname = models.CharField(max_length=200)
    num_table = models.IntegerField(default=0)
    menu0 = models.CharField(max_length=20)
    menu1 = models.CharField(max_length=20)
    menu2 = models.CharField(max_length=20)
    menu3 = models.CharField(max_length=20)
    menu4 = models.CharField(max_length=20)
    menu5 = models.CharField(max_length=20)
    menu6 = models.CharField(max_length=20)
    menu7 = models.CharField(max_length=20)
    menu8 = models.CharField(max_length=20)
