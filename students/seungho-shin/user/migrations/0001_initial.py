# Generated by Django 3.2 on 2021-05-03 12:38

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, null=True, unique=True)),
                ('nick_name', models.CharField(blank=True, max_length=45, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=45, unique=True)),
                ('phone_number', phone_field.models.PhoneField(blank=True, max_length=31, unique=True)),
            ],
            options={
                'db_table': 'signups',
            },
        ),
    ]
