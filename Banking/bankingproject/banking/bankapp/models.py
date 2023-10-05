from django.db import models
from django.forms import ModelForm
# Create your models here.

import datetime
class District(models.Model):
    name=models.CharField(max_length=250,blank=True,null=True)

    def __str__(self):
        return self.name
class Branches(models.Model):
    district=models.ForeignKey(District,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.name
accounttype_CHOICES=[
    ("Savings account" ,"Savings account"),
    ("Current account","Current account")
    ]
class Application(models.Model):

    name = models.CharField(max_length =250, default = None)
    DOB = models.DateField(auto_now=False,auto_now_add=False)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length = 250,default = None)
    email = models.EmailField(default = None)
    phonenumber = models.PositiveIntegerField(default=0)

    address=models.CharField(max_length=250,default=None)
    district= models.ForeignKey(District,on_delete=models.CASCADE)
    branch = models.ForeignKey(Branches,on_delete=models.CASCADE)

    state = models.CharField(max_length=250)
    pincode = models.PositiveIntegerField()
    accounttype=models.CharField(max_length=250,choices=accounttype_CHOICES,default=None)
    materials_provided=models.CharField(max_length=250)

    def __str__(self):
        return self.name
