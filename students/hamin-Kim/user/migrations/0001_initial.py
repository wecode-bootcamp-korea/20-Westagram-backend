# Generated by Django 3.2 on 2021-05-04 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=45)),
                ('nickname', models.CharField(blank=True, max_length=20)),
                ('phonenumber', models.CharField(blank=True, max_length=20)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
