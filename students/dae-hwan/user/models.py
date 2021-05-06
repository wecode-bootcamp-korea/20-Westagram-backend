from django.db import models

class User(models.Model):
    email        = models.CharField(max_length=254)
    password     = models.CharField(max_length=254) 
    nick_name    = models.CharField(max_length=45, blank = True)
    phone_number = models.CharField(max_length=45, blank = True)
    create_at    = models.DateTimeField(auto_now_add=True)
    update_at    = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.email
