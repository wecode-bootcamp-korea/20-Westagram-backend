from django.db      import models

from account.models import User

class Post(models.Model):
    user       = models.ForeignKey(User, on_delete=models.CASCADE)
    content    = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'posts'

class Image(models.Model):
    image_url = models.URLField(max_length=500)
    post      = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        db_table = 'images'