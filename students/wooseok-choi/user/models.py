from django.db import models

class User(models.Model):
    email         = models.CharField(max_length = 100)
    password      = models.BinaryField()
    phone_number  = models.CharField(max_length = 30, null=True)
    nickname      = models.CharField(max_length = 100, null=True)

    class Meta:
        db_table = 'users'