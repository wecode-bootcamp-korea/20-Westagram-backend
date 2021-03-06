from django.db import models

class User(models.Model):
    email           = models.EmailField(max_length=100, unique=True)
    password        = models.CharField(max_length=200)
    phone_number    = models.CharField(max_length=100, unique=True, null=True)
    nickname        = models.CharField(max_length=100, unique=True, null=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'