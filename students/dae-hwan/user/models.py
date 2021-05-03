from django.db import models

from user.models import User

class Posting(models.Model):
    user      = models.ForeignKey('User', on_delete = models.CASCADE)
    content   = models.CharField(max_length = 100)
    like      = models.IntegerField(default = 0)
    create_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeFIeld(auto_now = True)

    class Meta:
        db_table = 'postings'

    def __str__(self):
        return self.user

class Image(models.Model):
    user      = models.ForeignKey('Posting', on_delete = models.CASCADE)
    

