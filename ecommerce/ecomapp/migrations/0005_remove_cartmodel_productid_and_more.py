# Generated by Django 4.1.5 on 2023-01-31 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0004_cartmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartmodel',
            name='productid',
        ),
        migrations.RemoveField(
            model_name='uploadmodel',
            name='productid',
        ),
    ]
