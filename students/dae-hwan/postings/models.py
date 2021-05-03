from django.db    import models
from user.models  import User

class Posting(models.Model):
    user      = models.ForeignKey(User, on_delete = models.CASCADE)
    content   = models.CharField(max_length = 1000)
    image_url = models.URLField(max_length = 1000)
    create_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'postings'


