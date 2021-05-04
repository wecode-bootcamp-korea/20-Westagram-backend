from django.db      import models

from account.models import User

class Post(models.Model):
    user       = models.ForeignKey(User, on_delete=models.CASCADE)
    image_url  = models.URLField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'posts'
