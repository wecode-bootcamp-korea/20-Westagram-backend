from django.db import models

class User(models.Model):
    email    = models.CharField(max_length=254)
    password = models.CharField(max_length=1000)
    phone    = models.CharField(max_length=15, null=True) 
    nickname = models.CharField(max_length=26, null=True)

    def __str__(self):
        return self.email

    class Meta:
        db_table = "users"

