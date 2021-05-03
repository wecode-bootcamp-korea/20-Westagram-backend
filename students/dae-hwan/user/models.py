from django.db import models

class User(models.Model):
    email     = models.CharField(max_length=254)
    password  = models.CharField(max_length=254)

    class Meta:
        db_table = 'users'
