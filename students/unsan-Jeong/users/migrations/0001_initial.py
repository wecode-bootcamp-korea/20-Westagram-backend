# Generated by Django 3.2 on 2021-05-03 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=64, verbose_name='user e-mail')),
                ('name', models.CharField(max_length=32, verbose_name='use name')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('phone_number', models.CharField(max_length=11, verbose_name='phone number')),
                ('nickname', models.CharField(max_length=32, verbose_name='nickname')),
                ('age', models.IntegerField(blank=True, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
