# Generated by Django 5.1rc1 on 2024-08-30 01:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Appkim', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profesor',
            name='profesion',
        ),
    ]
