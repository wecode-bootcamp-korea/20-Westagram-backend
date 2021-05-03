from django.db    import models

from users.models import User

class Post(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    img_url = models.CharField(max_length=2000)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'posts'