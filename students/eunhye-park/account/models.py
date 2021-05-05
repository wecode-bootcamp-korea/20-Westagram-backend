from django.db import models
class User(models.Model):
    email        = models.EmailField(max_length=80)
    password     = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=80)
    username     = models.CharField(max_lenght=80)

    class Meta:
        db_table: "users"