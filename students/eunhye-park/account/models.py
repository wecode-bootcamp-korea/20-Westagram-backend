from django.db import models
class User(models.Model):
    email        = models.EmailField(max_length=80)
    password     = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=80, null = True)
    nickname     = models.CharField(max_length=80, null = True)

    class Meta:
        db_table: "users"