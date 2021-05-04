# Generated by Django 3.2 on 2021-05-04 05:00

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20210504_0246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nick_name',
            field=models.CharField(max_length=45, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=phone_field.models.PhoneField(max_length=45, unique=True),
        ),
    ]
