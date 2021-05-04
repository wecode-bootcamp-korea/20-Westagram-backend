# Generated by Django 3.2 on 2021-05-03 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210502_1423'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='created_at',
            new_name='create_at',
        ),
        migrations.RemoveField(
            model_name='user',
            name='modified_at',
        ),
        migrations.AddField(
            model_name='user',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]