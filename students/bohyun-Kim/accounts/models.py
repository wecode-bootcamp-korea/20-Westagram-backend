from django.db import models

# Create your models here.
class User(models.Model):
    phone_number = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.BinaryField(max_length = 500)

    class Meta:
        db_table = 'users'