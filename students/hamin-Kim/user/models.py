from django.db import models


class Users(models.Model):
    email       = models.CharField(max_length=45, unique=True)
    password    = models.IntegerField()
    nickname    = models.CharField(max_length=20, unique=True, blank=True)
    phonenumber = models.IntegerField(unique=True, blank=True)
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)

    class Meta:
        db_table = 'users'