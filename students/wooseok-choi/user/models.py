from django.db import models

class User(models.Model):
    email        = models.CharField(max_length = 254)
    password     = models.CharField(max_length = 80)
    phone_number = models.CharField(max_length = 30, null=True, blank=True)
    nickname     = models.CharField(max_length = 60, null=True, blank=True)

    class Meta:
        db_table = 'users'
