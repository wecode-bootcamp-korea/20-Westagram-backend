from django.db import models


class User(models.Model):
    email       = models.EmailField(max_length=200, unique=True)
    password    = models.CharField(max_length=100)
    nickname    = models.CharField(max_length=45, null=True, unique = True)
    phone       = models.IntegerField(null=True, unique = True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'
