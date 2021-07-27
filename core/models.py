from django.db import models


class message(models.Model):
    mesgcont= models.CharField(max_length=1000,blank=True,null=True)
    source = models.CharField(max_length=1000,null=True,blank=True)
    conttype= models.CharField(max_length=20,null=True,blank=True,default="text")
    sender= models.CharField(max_length=100,null=True,blank=True)
    countrycode= models.CharField(max_length=5,null=True,blank=True,default="91")
    dialcode= models.CharField(max_length=20,null=True,blank=True)
# Create your models here.


class customer(models.Model):
    number= models.CharField(max_length=1000,primary_key=True)
    last_product_id=models.IntegerField(null=True,blank=True)
    product_searched= models.CharField(max_length=1000,null=True,blank=True)
    

class products(models.Model):
    name=models.CharField(max_length=1000)
    #price=models.IntegerField(null=True,blank=True)
    price=models.CharField(max_length=1000,default='100.11')
    short_desc=models.CharField(max_length=1000)
    page=models.URLField()