from django.db import models


class message(models.Model):
    mesgcont= models.CharField(max_length=1000,blank=True,null=True)
    source = models.CharField(max_length=1000,null=True,blank=True)
    conttype= models.CharField(max_length=20,null=True,blank=True,default="text")
    sender= models.CharField(max_length=100,null=True,blank=True)
    countrycode= models.CharField(max_length=5,null=True,blank=True,default="91")
    dialcode= models.CharField(max_length=20,null=True,blank=True)
# Create your models here.
