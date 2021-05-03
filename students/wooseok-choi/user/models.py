from django.db import models

# Create your models here.
class User(models.Model):
    user_email = models.CharField(max_length = 45)
    user_password = models.CharField(max_length = 45)
    phone_number = models.CharField(max_length = 45)
    nickname = models.CharField(max_length = 45)

    class Meta:
        db_table = 'users'
