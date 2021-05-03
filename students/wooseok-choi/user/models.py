from django.db import models


class User(models.Model):
    email        = models.CharField(max_length = 45)
    password     = models.CharField(max_length = 20)
    phone_number = models.CharField(max_length = 15)
    nickname     = models.CharField(max_length = 40)

    class Meta:
        db_table = 'users'

