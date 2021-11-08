from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.db.models.fields import related

# Create your models here.
class UserDetail(models.Model):
    # user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    
    name=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
            return self.name



# class Tag(models.Model):
# 	name = models.CharField(max_length=200, null=True)

# 	def __str__(self):
# 		return self.name


class UserProduct(models.Model):
    
    PRODUCT_TYPE =(        
        ('ACER','ACER'),
        ('DELL','DELL'),
        ('HP','HP'),
        ('SAMSUNG','SAMSUNG'),
        ('LENOVO','LENOVO'),
        ('MACBOOK','MACBOOK'),
        ('MI NOTEBOOK','MI NOTEBOOK'),
        ('ASUS','ASUS'),

    )
    user=models.ForeignKey(User,on_delete=CASCADE ,default=1)
    productname=models.CharField(max_length=200, null=True)   
    producttype = models.CharField(max_length=100, choices=PRODUCT_TYPE, default='laptop')
    serialnumber=models.CharField(max_length=200,null=True)
    Date_Of_Purchase=models.DateField("Date_Of_Purchase(dd/mm/yyyy)",auto_now_add=False,auto_now=False,blank=True,null=True)
    # tags = models.ManyToManyField(Tag)
    def __str__(self):
            return self.productname


class statusdata(models.Model):
    STATUS=(
        ('Pending','Pending'),
        ('UnderProcess','UnderProcess'),
        ('Returned','Returned'),
    )
    # username=models.ForeignKey(User,on_delete=CASCADE ,default=1)
    # productname= models.ForeignKey(UserProduct, null=True, on_delete= models.SET_NULL)
    date_created=models.DateTimeField(auto_now_add=True,null=True,)
    status=models.CharField(max_length=100,null=True,choices=STATUS)
    