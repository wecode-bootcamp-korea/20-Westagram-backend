from django.db              import models

# Create your models here.

class Signin(models.Model):
    nick_name   =models.CharField(max_length=45, unique=True, blank=True)
    email       =models.CharField(max_length=45, unique=True)
    password    =models.CharField(max_length=250)
    phone_number=models.CharField(max_length=20, unique=True, blank=True)

    class Meta:
          db_table = 'signin'
