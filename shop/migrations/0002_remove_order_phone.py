# Generated by Django 3.2 on 2024-05-29 03:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='phone',
        ),
    ]
