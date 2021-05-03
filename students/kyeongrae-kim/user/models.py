from django.db  import models

class User(models.Model):
    mobile_num      = models.CharField(max_length=255)
    email           = models.CharField(max_length=255)
    username        = models.CharField(max_length=255)
    password        = models.CharField(max_length=255)
    created_at      = models.DateTimeField(auto_now_add=True)
    modified_at     = models.DateField(auto_now=True)

    class Meta:
        db_table = 'users'