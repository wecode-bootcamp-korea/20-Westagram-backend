from django.db              import models

# Create your models here.

class User(models.Model):
    nick_name   =models.CharField(max_length=45, unique=True, null=True)
    email       =models.CharField(max_length=100, unique=True)
    password    =models.CharField(max_length=200)
    phone_number=models.CharField(max_length=20, null=True)

    class Meta:
          db_table = 'users'