from django.db import models

class Users(models.Model):
    id           = models.BigAutoField(primary_key= True)
    email        = models.EmailField(max_length=128, verbose_name="user e-mail")
    name         = models.CharField(max_length =32, verbose_name="use name")
    password     = models.CharField(max_length=128, verbose_name="password")
    phone_number = models.CharField(max_length=32, verbose_name="phone number")
    nickname     = models.CharField(max_length=32, verbose_name="nickname")
    age          = models.IntegerField(null=True, blank=True)
    create_at    = models.DateTimeField(auto_now_add=True)
    update_at    = models.DateTimeField(auto_now =True)
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = "users"
