from django.db import models


class User(models.Model):
    email    = models.EmailField(max_length=200)
    password = models.CharField(max_length=100)
    nickname = models.CharField(max_length=45, null=True)
    phone    = models.IntegerField(null=True)

    class Meta:
        db_table = 'users'
