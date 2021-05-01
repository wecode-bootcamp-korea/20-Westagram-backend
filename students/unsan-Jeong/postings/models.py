from django.db import models

from users.models import Users
# Create your models here.
class Postings(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_name = models.CharField(max_length=32)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name = "user", related_name="post")
    image_url = models.URLField(max_length=64)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "posting"
        