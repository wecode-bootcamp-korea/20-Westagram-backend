from django.db           import models
from django.forms.models import model_to_dict


class User(models.Model):

    email = models.EmailField(
        "user email",
        max_length=254,
        unique=True,
        blank=False,
    )
    password = models.CharField(
        "user password",
        max_length=50,
        blank=False,
    )

    username = models.CharField(
        "user nickname",
        max_length=50,
        unique=True,
        null=True,
    )

    phone_number = models.CharField(
        "user phone number",
        max_length=17,
        unique=True,
        null=True,
    )

    class Meta:
        app_label = "users"
        db_table = "users"

    def __str__(self):
        return self.email

    def to_dict(self):
        model_dict = model_to_dict(self)
        model_dict.pop("password")
        return model_dict
