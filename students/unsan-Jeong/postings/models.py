from django.db import models

from users.models import Users

class Postings(models.Model):
    id        = models.BigAutoField(primary_key=True)
    name      = models.CharField(max_length=32)
    user_name = models.CharField(max_length=32)
    user      = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name = "user", related_name="post")
    image_url = models.URLField(max_length=64)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "posting"
        
class Comments(models.Model):
    id        = models.BigAutoField(primary_key=True)
    post      = models.ForeignKey("Postings", on_delete=models.CASCADE, verbose_name = "post", related_name="comment")
    user      = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name = "user", related_name="comment")
    create_at = models.DateTimeField(auto_now_add=True)
    content   = models.TextField()

    class Meta:
        db_table = "comment"