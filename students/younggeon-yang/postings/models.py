from django.db   import models

from user.models import User

class Post(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    time_create = models.DateTimeField(auto_now_add=True)
    img_url     = models.CharField(max_length=1000)
    text        = models.CharField(max_length=2000)

    def __str__(self):
        return self.text

    class Meta:
        db_table = "posts"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    time_create = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=2000)

    def __str__(self):
        return self.text

    class Meta:
        db_table = "comments"
