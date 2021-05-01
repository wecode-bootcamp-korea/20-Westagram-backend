from django.db import models

# Create your models here.
class User(models.Model):
    id = models.CharField(max_length = 45)
    password = models.CharField(max_length = 45)

    class Meta:
        db_table = 'users'

