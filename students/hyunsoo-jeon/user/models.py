from django.db   import models


class User(models.Model):
    email        = models.EmailField(max_length=50, unique=True) 
    password     = models.CharField(max_length=100) 
    nickname     = models.CharField(max_length=100, unique=True, null=True)
    phone_number = models.CharField(max_length=100, unique=True, null=True)

    class Meta():
        db_table = 'users'

