from django.db import models


class Users(models.Model):
    email       = models.CharField(max_length=80)
    password    = models.CharField(max_length=80)
    nickname    = models.CharField(max_length=50, blank=True)
    phonenumber = models.CharField(max_length=50, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nickname

    class Meta:
        db_table = 'users'