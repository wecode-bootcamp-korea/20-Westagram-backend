from django.db import models

class User(models.Model):
    email    = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    phone    = models.CharField(max_length=45, null=True) 
    nickname = models.CharField(max_length=45, null=True)

    def __str__(self):
        return self.email

    class Meta:
        db_table = "users"

