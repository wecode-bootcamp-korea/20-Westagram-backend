from django.db import models

class Users(models.Model):
    email        = models.EmailField(max_length=128)
    name         = models.CharField(max_length =32)
    password     = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=32)
    nickname     = models.CharField(max_length=32)
    age          = models.IntegerField(null=True, blank=True)
    create_at    = models.DateTimeField(auto_now_add=True)
    update_at    = models.DateTimeField(auto_now =True)
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = "users"
        
