from django.db   import models

from phone_field import PhoneField

# Create your models here.
class User(models.Model):
        name         = models.CharField(max_length=45,null=True)
        nick_name    = models.CharField(max_length=45, unique=True)
        password     = models.CharField(max_length=100)
        email        = models.CharField(max_length=45, unique=True)
        phone_number = models.CharField(max_length=11, unique=True)

        class Meta:
            db_table = 'users'