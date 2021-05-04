from django.db import models
class User(models.Model):
    username     = models.CharField(max_lenght=45)
    password     = models.CharField(max_length=45)
    email        = models.EmailField(max_length=45)
    name         = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=45)

    class Meta:
        db_table: "users"