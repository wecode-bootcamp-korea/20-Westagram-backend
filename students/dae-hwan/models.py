from django.db import models

class Posting(models.model):
    user = models.ForeignKey(
