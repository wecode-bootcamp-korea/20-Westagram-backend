# Generated by Django 3.2 on 2021-05-04 01:31

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
                ('email', models.EmailField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('nickname', models.CharField(max_length=45, null=True, unique=True)),
                ('phone', models.CharField(max_length=20, null=True, unique=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
