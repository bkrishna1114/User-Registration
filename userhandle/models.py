from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser

class user(AbstractBaseUser):
    first_name = models.CharField(max_length=100,blank=False)
    last_name = models.CharField(max_length=100,blank=True)
    email = models.CharField(max_length=100,unique=True,blank=False)
    phone_number = models.CharField(max_length=20,blank=False)
    address = models.CharField(max_length=200,blank=False)
    pincode = models.CharField(max_length=6,blank=False)
    company_name = models.CharField(max_length=50,blank=False)
    password = models.CharField(max_length=35,blank=False)
    user_name = 'email'
    required_fields = []

    #making table name here...
    class Meta:
        db_table ='user'