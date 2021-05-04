from django.db                     import models

from phone_field import PhoneField

# Create your models here.
class User(models.Model):
        name         = models.CharField(max_length=45, null=True, blank=False,)
        nick_name    = models.CharField(max_length=45, null=False, blank=True, unique=True)
        password     = models.CharField(max_length=100, null=False, blank=False)
        email        = models.CharField(max_length=45, null=False, blank=False, unique=True)
        phone_number = PhoneField(max_length=45, null=False, blank=True, unique=True)

        class Meta:
            db_table = 'users'

    