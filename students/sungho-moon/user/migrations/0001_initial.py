# Generated by Django 3.2 on 2021-05-06 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick_name', models.CharField(max_length=45, null=True, unique=True)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=20, null=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
