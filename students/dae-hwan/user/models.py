from django.db import models

class User(models.Model):
    email        = models.CharField(max_length=254)
    password     = models.CharField(max_length=254) 
    nick_name    = models.CharField(max_length=45, null = True)
    phone_number = models.CharField(max_length=45, null=True)
    create_at    = models.DateTimeField(auto_now_add=True)
    update_at    = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.nick_name
