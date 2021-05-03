from django.db              import models

# Create your models here.

class Signup(models.Model):
    nick_name   =models.CharField(max_length=45, unique=True)
    email       =models.CharField(max_length=45, unique=True)
    password    =models.CharField(max_length=45)
    phone_number=models.CharField(max_length=20, unique=True)

    class Meta:
          db_table = 'signup'


